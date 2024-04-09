import { createRouter, createWebHistory } from 'vue-router';
import RegistrationForm from '@/components/RegistrationForm.vue';
import FlashcardCreationForm from '@/components/FlashcardCreationForm.vue';
import CategoryCreationForm from '@/components/CategoryCreationForm.vue';

const routes = [
  {
    path: '/register',
    name: 'Register',
    component: RegistrationForm,
  },
  {
    path: '/create-flashcard',
    name: 'CreateFlashcard',
    component: FlashcardCreationForm,
  },
  {
    path: '/create-category',
    name: 'CreateCategory',
    component: CategoryCreationForm,
  },
  // Weitere Routen hier hinzufügen
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
