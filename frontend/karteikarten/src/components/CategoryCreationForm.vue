<template>
  <div>
    <h2>Kategorie erstellen</h2>
    <form @submit.prevent="submitCategory">
      <input type="text" v-model="name" placeholder="Kategoriename" />
      <button type="submit">Erstellen</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      user_id: ''
    };
  },
  mounted() {
    this.user_id = localStorage.getItem('user_id');
    if (!this.user_id) {
      console.error("Keine Benutzer-ID gefunden. Bitte stellen Sie sicher, dass der Benutzer angemeldet ist.");
      // Optional: Weiterleitung zur Anmeldeseite oder Anzeige einer Warnung.
    }
  },
  methods: {
    async submitCategory() {
      if (!this.user_id) {
        console.error("Aktion nicht möglich. Keine Benutzer-ID verfügbar.");
        return;
      }
      try {
        const response = await axios.post(`http://127.0.0.1:8000/users/${this.user_id}/categories`, {
          name: this.name,
          user_id: parseInt(this.user_id)
        });
        
        console.log("Kategorie erstellt:", response.data);
        // Implementiere hier die Erfolgslogik, z.B. Benachrichtigung oder Weiterleitung
      } catch (error) {
        console.error("Fehler beim Erstellen der Kategorie:", error);
        // Fehlerbehandlung, z.B. Anzeige einer Fehlermeldung
      }
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

input[type="text"] {
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
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>