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
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      user_id: '',  // Initialwert, wird im mounted Lifecycle Hook gesetzt
    };
  },
  mounted() {
    this.user_id = localStorage.getItem('user_id');  // Lade user_id beim Start der Komponente
    if (!this.user_id) {
      console.error("Keine Benutzer-ID gefunden. Bitte stellen Sie sicher, dass der Benutzer angemeldet ist.");
      // Optional können Sie den Benutzer zurück zur Anmeldeseite leiten oder eine Warnmeldung anzeigen.
    }
  },
  methods: {
    async submitCategory() {
      if (!this.user_id) {
        console.error("Aktion nicht möglich. Keine Benutzer-ID verfügbar.");
        return; // Beende die Funktion frühzeitig, wenn keine user_id vorhanden ist
      }
      try {
        const response = await axios.post(`http://127.0.0.1:8000/users/${this.user_id}/categories`, {
          name: this.name,
          user_id: parseInt(this.user_id)  // Stelle sicher, dass dies eine Zahl ist
        });
        
        console.log("Kategorie erstellt:", response.data);
        // Erfolgslogik hier
      } catch (error) {
        console.error("Fehler beim Erstellen der Kategorie:", error);
        // Fehlerbehandlung hier
      }
    }
  }
};
</script>