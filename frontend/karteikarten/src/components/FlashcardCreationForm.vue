<template>
  <div>
    <h2>Karteikarte erstellen</h2>
    <form @submit.prevent="submitFlashcard">
      <input v-model="question" placeholder="Frage" required />
      <input v-model="answer" placeholder="Antwort" required />
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
  methods: {
    async loadCategories() {
      if (!this.user_id) return; // Frühzeitiges Beenden, wenn keine user_id vorhanden ist
      try {
        const response = await axios.get(`http://127.0.0.1:8000/users/${this.user_id}/categories`);
        this.categories = response.data;
      } catch (error) {
        console.error('Fehler beim Laden der Kategorien:', error);
      }
    },
    async submitFlashcard() {
      try {
        const response = await axios.post(`http://127.0.0.1:8000/users/${this.user_id}/flashcards`, {
          question: this.question,
          answer: this.answer,
          category_id: parseInt(this.category_id),
          owner_id: parseInt(this.user_id) // Verwende user_id als owner_id
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
      this.categories = [];
    }
  },
  mounted() {
    this.user_id = localStorage.getItem('user_id'); // Abrufen der user_id aus dem LocalStorage
    this.loadCategories();
  }
};
</script>
