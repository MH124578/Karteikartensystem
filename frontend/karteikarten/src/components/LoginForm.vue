<template>
    <div>
      <h2>Anmelden</h2>
      <form @submit.prevent="login">
        <input v-model="email" type="email" placeholder="E-Mail" required />
        <input v-model="password" type="password" placeholder="Passwort" required />
        <button type="submit">Anmelden</button>
      </form>
      <router-link to="/register">Registrieren</router-link> |
      <router-view/>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import router from '../router';
  
  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
        async login() {
        console.log("Sending:", this.email, this.password);
        try {
            const response = await axios.post('http://127.0.0.1:8000/login', {
            email: this.email,
            password: this.password,
            });
            console.log('Login successful:', response.data); // Stellen Sie sicher, dass diese Zeile die `user_id` anzeigt
            // Speichern der user_id im LocalStorage
            localStorage.setItem('user_id', response.data.user_id);
            this.$emit('login-success');
            router.push('/dashboard');
        } catch (error) {
            if (error.response && error.response.data && error.response.data.detail) {
            console.error('Fehler beim Anmelden:', error.response.data.detail);
            } else {
            console.error('Fehler beim Anmelden:', error);
            }
        }
        }
    }
  };
  </script>