import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../components/QuestionsManager.vue'
import ScoresPage from '../views/ScoresPage.vue'
import Login from '../views/Login.vue'
import ListQuestionPage from '../views/ListQuestionsPage.vue'
import Logout from '../views/Logout.vue'
import QuestionAdmin from '../views/QuestionAdminDisplay.vue'
import AdminSpace from '../views/AdminSpacePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/newQuiz',
      name: 'New Quiz',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'Quiz',
      component: QuestionsManager
    },
    {
      path: '/scores',
      name: 'Scores',
      component: ScoresPage
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout
    },
    {
      path: '/DataList',
      name: 'DataList',
      component: ListQuestionPage
    },
    {
      path: '/AdminSpace',
      name: 'AdminSpace',
      component: AdminSpace,
      props: true
    },
    {
      path: '/adminDisplay',
      name: 'adminDisplay',
      component: QuestionAdmin,
      props: true
    }

  ]
})

export default router
