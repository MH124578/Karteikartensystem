<template>
  <div>
    <h2>Kategorie erstellen</h2>
    <form @submit.prevent="submitCategory">
      <input v-model="name" placeholder="Kategoriename" />
      <button type="submit">Erstellen</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
    };
  },
  methods: {
    async submitCategory() {
      try {
        const response = await this.axios.post('/users/{user_id}/categories/', {
          name: this.name
        });
        console.log(response.data);
        // Erfolgslogik hier
      } catch (error) {
        console.error(error);
        // Fehlerbehandlung hier
      }
    }
  }
};
</script>
