<template>
  <div class="anmelden">
    <h2>Anmelden</h2>
    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="E-Mail" required />
      <input v-model="password" type="password" placeholder="Passwort" required />
      <button type="submit">Anmelden</button>
    </form>
    <router-link to="/register" class="registration-link">Noch keinen Account? Hier Registrieren</router-link>
  </div>
  <router-view />
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async login() {
      console.log("Versuche anzumelden mit:", this.email, this.password);
      try {
        const response = await axios.post('http://127.0.0.1:8000/login', {
          email: this.email,
          password: this.password,
        });
        console.log('Login erfolgreich:', response.data);
        localStorage.setItem('user_id', response.data.user_id);
        this.$emit('login-success');
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Fehler beim Anmelden:', error.response ? error.response.data.detail : error);
      }
    }
  }
};
</script>

<style scoped>
.center {
  display: flex;
  flex-direction: column; /* Stellt die Elemente vertikal ein */
  justify-content: center; /* Zentriert die Elemente vertikal */
  align-items: center; /* Zentriert die Elemente horizontal */
  min-height: 100vh; /* Mindesthöhe, damit es den gesamten Bildschirm einnimmt */
}

form {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 300px; /* Setzt die maximale Breite des Formulars */
  margin: 0 auto; /* Fügt automatische Seitenränder hinzu, um horizontal zu zentrieren */
}

input[type="email"], input[type="password"] {
  width: calc(100% - 20px); /* passt die Breite an, um Padding zu berücksichtigen */
  padding: 10px;
  margin-bottom: 10px; /* Nur der untere Abstand, um nicht doppelt zu zählen */
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: calc(100% - 20px); /* passt die Breite an, um Padding zu berücksichtigen */
  box-sizing: border-box;
}

button:hover {
  background-color: #218838;
}

.registration-link {
  margin-top: 15px; /* Abstand über dem Registrierungslink */
  display: flex;
  flex-direction: column; /* Stellt die Elemente vertikal ein */
  justify-content: center; /* Zentriert die Elemente vertikal */
  align-items: center; /* Zentriert die Elemente horizontal */
  color: #007bff;
}

.anmelden{
  display: flex;
  flex-direction: column; /* Stellt die Elemente vertikal ein */
  justify-content: center; /* Zentriert die Elemente vertikal */
  align-items: center; /* Zentriert die Elemente horizontal */
}
</style>