<template>
  <div class="dashboard">
    <select v-model="selectedCategoryId" @change="updateSelectedCategory(selectedCategoryId)">
      <option disabled value="">Bitte wählen Sie eine Kategorie</option>
      <option v-for="category in categories" :key="category.id" :value="category.id">
        {{ category.name }}
      </option>
    </select>

    <p v-if="noFlashcardsMessage">{{ noFlashcardsMessage }}</p>

    <div v-for="(column, columnIndex) in columns" :key="columnIndex" class="column">
      <h2>{{ column.title }}</h2>
      <div v-for="(card, cardIndex) in column.cards" :key="card.id" class="card" @click="selectCard(card)">
        <div>{{ card.question }}</div>
        <div class="card-actions">
          <button @click.stop="moveCard(columnIndex, cardIndex, -1)" :disabled="columnIndex === 0">← Zurück</button>
          <button @click.stop="moveCard(columnIndex, cardIndex, 1)" :disabled="columnIndex === columns.length - 1">Weiter →</button>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal" @click.self="closeModal">
      <div class="modal-content">
        <h3>{{ selectedCard.question }}</h3>
        <button @click="showAnswer = !showAnswer">Antwort zeigen</button>
        <p v-if="showAnswer">{{ selectedCard.answer }}</p>
        <button @click="closeModal">Schließen</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedCategoryId: null,
      categories: [],
      columns: [
        { title: '1', cards: [] },
        { title: '2', cards: [] },
        { title: '3', cards: [] },
        { title: '4', cards: [] },
        { title: '5', cards: [] }
      ],
      noFlashcardsMessage: '',
      showModal: false,
      selectedCard: null,
      showAnswer: false
    };
  },
  mounted() {
    this.loadCategories();
    this.loadCategories();
    this.restoreColumnsState();
  },
  methods: {
    async loadCategories() {
      const userId = localStorage.getItem('user_id');
      try {
        const response = await axios.get(`http://127.0.0.1:8000/users/${userId}/categories`);
        this.categories = response.data;
      } catch (error) {
        console.error('Fehler beim Laden der Kategorien:', error);
      }
    },
    async loadFlashcards() {
      if (!this.selectedCategoryId) return;
      
      // Versuche, den Zustand aus localStorage zu laden
      const columnsData = localStorage.getItem(`columnsData-${this.selectedCategoryId}`);
      if (columnsData) {
        const columns = JSON.parse(columnsData);
        this.columns = columns.map(column => ({
          title: column.title,
          cards: column.cards
        }));
      } else {
        this.columns.forEach(column => column.cards = []); // Reset cards in all columns initially
      }

      try {
        const response = await axios.get(`http://127.0.0.1:8000/flashcards?category_id=${this.selectedCategoryId}`);
        if (response.data.length > 0) {
          const newCards = response.data.filter(card => 
            !this.columns.some(column => 
              column.cards.some(storedCard => storedCard.id === card.id)
            )
          );

          if (newCards.length > 0) {
            this.columns[0].cards.push(...newCards); // Add new cards to the first column
            this.saveColumnsState(); // Update local storage with new state
          }
        }
      } catch (error) {
        console.error('Ein unbekannter Fehler ist aufgetreten:', error);
      }
    },
    updateSelectedCategory(categoryId) {
      this.selectedCategoryId = categoryId;
      this.loadFlashcards();
      this.restoreColumnsState();
    },
    selectCard(card) {
      this.selectedCard = card;
      this.showModal = true;
      this.showAnswer = false;
    },
    closeModal() {
      this.showModal = false;
      this.selectedCard = null;
    },
    saveColumnsState() {
      if (!this.selectedCategoryId) return;
      const columnData = this.columns.map(column => ({
        title: column.title,
        cards: column.cards.map(card => ({ 
          id: card.id, 
          question: card.question, 
          answer: card.answer 
        }))
      }));
      localStorage.setItem(`columnsData-${this.selectedCategoryId}`, JSON.stringify(columnData));
    },
    restoreColumnsState() {
      if (!this.selectedCategoryId) return;
      const columnsData = localStorage.getItem(`columnsData-${this.selectedCategoryId}`);
      if (columnsData) {
        const columns = JSON.parse(columnsData);
        this.columns = columns.map(column => ({
          title: column.title,
          cards: column.cards
        }));
      } else {
        this.columns = this.columns.map(column => ({ ...column, cards: [] }));
      }
    },
    moveCard(columnIndex, cardIndex, direction) {
      const toColumnIndex = columnIndex + direction;
      if (toColumnIndex < 0 || toColumnIndex >= this.columns.length) return;
      const card = this.columns[columnIndex].cards.splice(cardIndex, 1)[0];
      this.columns[toColumnIndex].cards.push(card);
      this.saveColumnsState();
    },
    
  }
};
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: #f2f3f5;
}

.category-select {
  margin: 10px 0;
  padding: 10px;
  width: 50%;
  background: white;
  border-radius: 4px;
}

.column {
  margin: 10px;
  padding: 10px;
  background: #ecf0f1;
  border-radius: 4px;
  width: 100%;
  max-width: 200px;
}

.card {
  margin: 5px;
  padding: 10px;
  background: #bdc3c7;
  border-radius: 4px;
  cursor: pointer;
}

.card-actions {
  display: flex;
  justify-content: space-between;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  padding: 20px;
  background: white;
  border-radius: 5px;
  width: 300px;
}
</style>

