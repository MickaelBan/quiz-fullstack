import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../components/QuestionsManager.vue'
import ScoresPage from '../views/ScoresPage.vue'
import Login from '../views/Login.vue'
import ListQuestionPage from '../views/ListQuestionsPage.vue'
import Logout from '../views/Logout.vue'
import QuestionAdmin from '../views/QuestionAdminDisplay.vue'
import EditQuestion from '../views/EditQuestionPage.vue'

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
      path: '/QuestionsList',
      name: 'QuestionsList',
      component: ListQuestionPage
    },
    {
      path: '/adminDisplay/:id',
      name: 'adminDisplay',
      component: QuestionAdmin,
      props: true
    },
    {
      path: '/EditQuestion/:id',
      name: 'EditQuestion',
      component: EditQuestion,
      props: true
    }

  ]
})

export default router
