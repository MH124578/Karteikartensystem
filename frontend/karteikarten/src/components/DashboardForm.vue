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
        { title: 'Spalte 1', cards: [] },
        { title: 'Spalte 2', cards: [] },
        { title: 'Spalte 3', cards: [] },
        { title: 'Spalte 4', cards: [] },
        { title: 'Spalte 5', cards: [] }
      ],
      noFlashcardsMessage: '',
      showModal: false,
      selectedCard: null,
      showAnswer: false
    };
  },
  mounted() {
    this.loadCategories();
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
      try {
        const response = await axios.get(`http://127.0.0.1:8000/flashcards?category_id=${this.selectedCategoryId}`);
        if (response.data.length === 0) {
          this.noFlashcardsMessage = 'Es gibt noch keine Flashcards in dieser Kategorie.';
          this.columns.forEach(column => column.cards = []);
        } else {
          this.noFlashcardsMessage = '';
          this.columns[0].cards = response.data;
        }
      } catch (error) {
        if (error.response && error.response.status === 404) {
          this.noFlashcardsMessage = 'Es gibt noch keine Flashcards in dieser Kategorie.';
          this.columns.forEach(column => column.cards = []);
        } else {
          console.error('Ein unbekannter Fehler ist aufgetreten:', error);
        }
      }
    },
    updateSelectedCategory(categoryId) {
      this.selectedCategoryId = categoryId;
      this.loadFlashcards();
    },
    selectCard(card) {
      this.selectedCard = card;
      this.showModal = true;
      this.showAnswer = false; // Verstecke die Antwort beim Öffnen des Modals
    },
    closeModal() {
      this.showModal = false;
      this.selectedCard = null;
    },
    moveCard(columnIndex, cardIndex, direction) {
      const toColumnIndex = columnIndex + direction;
      if (toColumnIndex < 0 || toColumnIndex >= this.columns.length) return;
      const card = this.columns[columnIndex].cards.splice(cardIndex, 1)[0];
      this.columns[toColumnIndex].cards.push(card);
    }
  }
};
</script>

<style scoped>
.dashboard {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  background: white;
}

.column {
  width: 18%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.card {
  padding: 10px;
  margin: 5px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  cursor: pointer;
}

.card-actions {
  display: flex;
  justify-content: space-between;
  padding-top: 10px;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  max-width: 500px;
  width: 90%;
  text-align: center;
}
</style>

