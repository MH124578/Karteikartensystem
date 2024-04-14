<template>
  <div>
    <h2>Registrierung</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Benutzername" />
      <input type="email" v-model="email" placeholder="E-Mail" />
      <input type="password" v-model="password" placeholder="Passwort" />
      <button type="submit">Registrieren</button>
    </form>
  </div>
</template>



<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/create_users/', {
          username: this.username,
          email: this.email,
          password: this.password,
        });
        console.log(response.data);
        // Weiterleitung oder Anzeige einer Erfolgsmeldung
      } catch (error) {
        // Überprüfe zuerst, ob error.response und error.response.data vorhanden sind
        if (error.response && error.response.data && error.response.data.detail) {
          console.error(error.response.data.detail);
        } else {
          // Allgemeiner Fehlerhandler, falls keine spezifischen Details vorhanden sind
          console.error("Ein Fehler ist aufgetreten.");
        }
      }
    },
  },
};
</script>
