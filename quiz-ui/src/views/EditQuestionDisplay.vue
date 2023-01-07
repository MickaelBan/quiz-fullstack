<template>
  <nav>
    <div class="cpnt">
      <form>
        <label for="title">
          <h5>Title</h5>
        </label>
        <input type="text" v-model="title" id="title" name="title" placeholder="title">
        <div v-if="title == ''" class="red">Title can't be empty</div>

        <label for="position">
          <h5>Position</h5>
        </label>
        <select v-model="position">
          <option disabled value="">Select position</option>
          <option v-for="index in sizeQuiz">{{ index }}</option>
        </select>
        <div v-if="position == ''" class="red">Position can't be empty</div>

        <label for=" text">
          <h5>Text</h5>
        </label>
        <input type="text" v-model="text" id="text" name="text" placeholder="text">
        <div v-if="text == ''" class="red">Text can't be empty</div>

        <label for="image">
          <h5>Image</h5>
        </label>
        <input type="text" v-model="image" id="image" name="image" placeholder="image">

        <label for="answers">
          <h5>Answers</h5>
        </label>
        <div class="table4">
          <div v-for="(answer, index) in answers">
            <div v-if="index + 1 == selected" class="correctAnswers">
              <label for="answer"> Answer: {{ index + 1 }}</label>
              <input id="answer" type="text" v-model="answer.text" placeholder="text">
            </div>
            <div v-else class="incorrectAnswers" v-on:click="selectAnswer(index + 1)">
              <label for="answer"> Answer: {{ index + 1 }}</label>
              <input id="answer" type="text" v-model="answer.text" placeholder="text">
            </div>
            <div v-if="answer.text == ''" class="red">Answer can't be empty</div>
          </div>
        </div>
      </form>
    </div>
    <div class="table">
      <div>
        <div class="button">
          <input type="submit" value="Cancel" v-on:click="$emit('cancel')">
        </div>
      </div>
      <div>
        <div class="button">
          <input type="submit" value="submit" v-on:click="send">
          <div class="red" v-if="invalidForm">Invalid</div>
        </div>
      </div>
    </div>
  </nav>

</template>
<style>
.table4 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.table4>div {
  padding: 1px;
  margin: 10px;
}
</style>
<script>
import QuizApiService from '../services/QuizApiService'
import AdminStorageService from '../services/AdminStorageService'
export default {
  emits: ['cancel', 'submit'],
  props: {
    sizeQuiz: Number,
    question: {
      title: String,
      text: String,
      id: Number,
      position: Number,
      image: String,
      possibleAnswers: Array
    }
  },
  data() {
    var title = this.question.title
    var text = this.question.text
    var image = this.question.image
    var answers = this.question.possibleAnswers
    var position = this.question.position
    var selected = 0
    var invalidForm = false

    return { text, title, position, image, answers, selected, invalidForm }
  },
  created() {
    console.log(this.sizeQuiz)
    for (var i = 0; i < this.answers.length; i++) {
      if (this.answers[i].isCorrect) {
        this.selected = i + 1
      }
    }
  },
  methods: {
    selectAnswer(index) {
      this.selected = index
    },
    validForm() {
      this.invalidForm = false;
      if (this.title == "" | this.text == "") {
        this.invalidForm = true;
      }
      for (var i = 0; i < this.answers.length; i++) {
        if (this.answers[i].text == "") {
          this.invalidForm = true;
        }
        if (i == this.selected - 1) {
          this.answers[i].isCorrect = true;
        }
        else {
          this.answers[i].isCorrect = false;
        }
      }
    },
    async send() {
      this.validForm()
      if (this.invalidForm) {
        return
      }
      console.log(this.answers)
      var token = AdminStorageService.getToken()
      await QuizApiService.putUpdateQuestion(this.question.id, this.title, this.position, this.text, this.image, this.answers, token)
      this.$router.go()
    }
  }
}
</script>