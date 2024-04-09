<template>
  <div>
    <h2>Karteikarte erstellen</h2>
    <form @submit.prevent="submitFlashcard">
      <input v-model="question" placeholder="Frage" />
      <input v-model="answer" placeholder="Antwort" />
      <select v-model="categoryId">
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
      <button type="submit">Erstellen</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      question: '',
      answer: '',
      categoryId: null,
      categories: [] // Für die Kategorienauswahl
    };
  },
  created() {
    this.fetchCategories();
  },
  methods: {
    fetchCategories() {
      // Implementiere Logik, um Kategorien vom Backend zu holen
    },
    async submitFlashcard() {
      // Implementiere die Logik, um eine Karteikarte zu erstellen
    }
  }
};
</script>

