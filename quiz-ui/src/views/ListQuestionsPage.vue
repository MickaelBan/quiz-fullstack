<template>
  <div v-if="!editQuestion">
    <div class="cpnt">
      <div class="button">
        <input type="submit" name="creationQuestion" value="Create question">
        <input type="submit" id="delAllQuestion" name="delQuestion" value="Delete all questions"
          v-on:click="deleteAllQuestion">
        <input type="submit" id="delAllParticipations" name="delAllParticipations" value="Delete all participations"
          v-on:click="delParticipations">
      </div>
    </div>
    <div class="table">
      <div>
        <div class="cpnt">
          <div class="title">
            <h1>List of question</h1>
          </div>
          <div class="list">
            <div class="score" v-for="question in questionsList" v-bind:key="question.id">
              <div v-on:click="seletedQuestion(question)">
                <h5>Title:</h5> {{ question.title }}
                <h5>Position:</h5> {{ question.position }}
                <h5>Text:</h5> {{ question.text }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>

        <div class="cpnt">
          <div class="title">
            <h1>List of participations</h1>
          </div>
          <div class="list">
            <div class="score" v-for="participation in participationsList" v-bind:key="participation.date">
              <h5>Name:</h5> {{ participation.playerName }}
              <h5>Score:</h5> {{ participation.score }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-else>
    <EditQuestionDisplay :question="currentQuestion" :sizeQuiz="sizeQuestionsList" @cancel="back" />
  </div>
</template>

<style>
.table {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>

<script>
import AdminStorageService from '../services/AdminStorageService';
import QuizApiService from '../services/QuizApiService';
import EditQuestionDisplay from './EditQuestionDisplay.vue';

export default {
  emits: ["question-selected"],
  components: {
    EditQuestionDisplay
  },
  data() {
    var questionsList = [];
    var participationsList = [];
    var sizeQuestionsList = 0;
    var editQuestion = false;
    var currentQuestion = {
      typeof: Object
    }
    return { questionsList, sizeQuestionsList, participationsList, editQuestion, currentQuestion }
  },
  async created() {
    var reponce = await QuizApiService.getQuizInfo()
    this.sizeQuestionsList = reponce.data.size
    this.participationsList = reponce.data.scores
    this.questionsList = await this.setQuestionsList()
  },
  methods: {
    async setQuestionsList() {
      var list = []
      for (var i = 1; i <= this.sizeQuestionsList; i++) {
        var question = await QuizApiService.getQuestionByPosition(i)
        list.push(question.data)
      }
      return list
    },
    seletedQuestion(question) {
      this.currentQuestion = question
      this.editQuestion = true
    },
    async deleteAllQuestion() {
      await QuizApiService.delAllQuestion(AdminStorageService.getToken())
      this.$router.go()
    },
    async delParticipations() {
      await QuizApiService.delAllParticipations(AdminStorageService.getToken())
      this.$router.go()
    },
    back() {
      this.editQuestion = false
    }
  }
}
</script>