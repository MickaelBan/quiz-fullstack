<template>
  <div class="cpnt">
    <div class="button">
      <input type="submit" name="creationQuestion" value="Create question">
    </div>
    <div class="title">
      <h1>List of question</h1>
    </div>
    <div class="list">
      <div class="score" v-for="question in questionsList" v-bind:key="question.id">
        {{ question.title }}
      </div>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';
export default {
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
    }
  }
}
</script>