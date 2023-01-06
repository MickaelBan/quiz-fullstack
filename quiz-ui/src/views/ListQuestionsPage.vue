<template>
  <div class="cpnt">
    <div class="button">
      <input type="submit" name="creationQuestion" value="Create question">
    </div>
  </div>

  <div class="title">
    <h1>List of question</h1>
  </div>
  <div class="cpnt">
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
</template>

<script>
import QuizApiService from '../services/QuizApiService';
export default {
  emits: ["question-selected"],
  data() {
    var questionsList = [];
    var sizeQuestionsList = 0;
    return { questionsList, sizeQuestionsList }
  },
  async created() {
    var reponce = await QuizApiService.getQuizInfo();
    this.sizeQuestionsList = reponce.data.size
    this.questionsList = await this.setQuestionsList()
  },
  methods: {
    async setQuestionsList() {
      var list = []
      for (var i = 1; i <= this.sizeQuestionsList; i++) {
        var question = await QuizApiService.getQuestionById(i)
        list.push(question.data)
      }
      return list
    },
    seletedQuestion(question) {
      this.$router.push("/adminDisplay")
      this.$emit("question-selected", question)
    }
  }
}
</script>