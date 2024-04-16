<template>
  <div>
    <h2>Karteikarte erstellen</h2>
    <form @submit.prevent="submitFlashcard">
      <input type="text" v-model="question" placeholder="Frage" required />
      <input type="text" v-model="answer" placeholder="Antwort" required />
      <select v-model="category_id" required>
        <option disabled value="">Bitte wähle eine Kategorie</option>
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
      <button type="submit">Erstellen</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      question: '',
      answer: '',
      category_id: '',
      user_id: null, // Initial null setzen, wird automatisch gefüllt
      categories: []
    };
  },
  mounted() {
    this.user_id = localStorage.getItem('user_id');
    this.loadCategories();
  },
  methods: {
    async loadCategories() {
      if (!this.user_id) return; // Keine Aktion, wenn keine Benutzer-ID vorhanden ist
      try {
        const response = await axios.get(`http://127.0.0.1:8000/users/${this.user_id}/categories`);
        this.categories = response.data;
      } catch (error) {
        console.error('Fehler beim Laden der Kategorien:', error);
      }
    },
    async submitFlashcard() {
      if (!this.user_id) {
        console.error('Aktion nicht möglich. Keine Benutzer-ID verfügbar.');
        return;
      }
      try {
        const response = await axios.post(`http://127.0.0.1:8000/users/${this.user_id}/flashcards`, {
          question: this.question,
          answer: this.answer,
          category_id: parseInt(this.category_id),
          owner_id: parseInt(this.user_id)
        });
        console.log('Karteikarte erstellt:', response.data);
        this.resetForm();
      } catch (error) {
        console.error('Fehler beim Erstellen der Karteikarte:', error);
      }
    },
    resetForm() {
      this.question = '';
      this.answer = '';
      this.category_id = '';
    }
  }
};
</script>

<style scoped>
form {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  margin: auto;
}

input[type="text"], select {
  width: calc(100% - 2px);
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #ff5722;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #e64a19;
}
</style>