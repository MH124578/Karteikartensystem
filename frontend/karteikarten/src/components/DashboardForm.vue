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
        <div v-for="(card, cardIndex) in column.cards" :key="card.id" class="card">
          <div>{{ card.question }}</div>
          <div>{{ card.answer }}</div>
          <button @click="moveCard(columnIndex, cardIndex, -1)" :disabled="columnIndex === 0">← Zurück</button>
          <button @click="moveCard(columnIndex, cardIndex, 1)" :disabled="columnIndex === columns.length - 1">Weiter →</button>
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
        noFlashcardsMessage: ''
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
          // Geeignete Fehlerbehandlung hier einfügen
        }
      },
      async loadFlashcards() {
        this.noFlashcardsMessage = ''; // Zurücksetzen der Nachricht
        if (!this.selectedCategoryId) return;
        try {
          const response = await axios.get(`http://127.0.0.1:8000/flashcards?category_id=${this.selectedCategoryId}`);
          this.columns[0].cards = response.data;
        } catch (error) {
          if (error.response && error.response.status === 404) {
            // Setze eine Nachricht, wenn keine Flashcards vorhanden sind
            this.noFlashcardsMessage = 'Es gibt noch keine Flashcards in dieser Kategorie.';
            this.columns.forEach(column => column.cards = []); // Klar die Karten in allen Spalten
          } else {
            console.error('Ein unbekannter Fehler ist aufgetreten:', error);
            // Geeignete Fehlerbehandlung hier einfügen
          }
        }
      },
      updateSelectedCategory(categoryId) {
        this.selectedCategoryId = categoryId;
        this.loadFlashcards();
      },
      moveCard(fromColumnIndex, cardIndex, direction) {
        const toColumnIndex = fromColumnIndex + direction;
        if (toColumnIndex < 0 || toColumnIndex >= this.columns.length) return;
        const card = this.columns[fromColumnIndex].cards.splice(cardIndex, 1)[0];
        this.columns[toColumnIndex].cards.push(card);
      }
    }
  };
  </script>
  
  <style>
  .dashboard {
    display: flex;
    justify-content: space-between;
  }
  .column {
    width: 18%; /* Berechne die Breite entsprechend */
    padding: 10px;
    border: 1px solid #ccc;
  }
  .card {
    padding: 10px;
    margin: 5px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
  }
  </style>
  