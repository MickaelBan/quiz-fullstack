<template>
  <div v-for="(question, index) in questionsList" v-bind:key="question.id">
    <div class="QuestionDislayAdmin">
      <div class="title">
        <h1>Question {{ index }}</h1>
      </div>
      <QuestionDisplay :question=question :adminMode=true />
      <div class="button" id="edit">
        <input type="submit" value="Edit question" v-on:click="editQuestion()">
      </div>
      <div class="button" id="delete">
        <input type="submit" value="Remove question" v-on:click="deleteQuestion">
      </div>
    </div>
  </div>





</template>

<style>
.QuestionDislayAdmin {
  width: 100%;
  margin: 100px 0px;
}
</style>


<script>
import AdminStorageService from '../services/AdminStorageService';
import QuizApiService from '../services/QuizApiService';
import QuestionDisplay from './QuestionDisplay.vue';
export default {
  components: { QuestionDisplay },
  data() {
    var questionsList = []
    var sizeQuestionsList = 0
    return { questionsList, sizeQuestionsList }
  },
  async created() {
    var reponce = await QuizApiService.getQuizInfo()
    this.sizeQuestionsList = reponce.data.size
    this.questionsList = await this.setQuestionsList()
    console.log(this.questionsList)
    console.log("created display question")
  },
  methods: {
    async deleteQuestion(question) {
      let token = AdminStorageService.getToken();
      if (token !== undefined) {
        await QuizApiService.delQuestion(token, question.id);
        this.$router.go();
      }
    },
    async setQuestionsList() {
      var list = []
      for (var i = 1; i <= this.sizeQuestionsList; i++) {
        var question = await QuizApiService.getQuestionByPosition(i)
        list.push(question.data)
      }
      return list
    }
  }
}
</script>