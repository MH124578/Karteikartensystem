import { createApp } from 'vue';
import App from './App.vue';
import { router } from './router';

// Erstelle eine Vue-Anwendung
const app = createApp(App);

// Verwende den Router mit der App-Instanz
app.use(router);

app.mount('#app');
