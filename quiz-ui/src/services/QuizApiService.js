import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestionById(id) {
    return this.call("get", "questions/" + id);
  },
  getQuestionByPosition(position) {
    return this.call("get", "questions?position=" + position);
  },
  postParticipation(username, answers) {
    var data = {
      "playerName": username,
      "answers": answers
    }
    return this.call("post", "participations", data)
  },
  postLogin(password) {
    //a refaire, peut être que password est deja un json, j'y connais rien
    var data = { "password": password }
    return this.call("post", "login", data)
  },
  postCreateQuestion(title = null, text = null, image = null, possibleAnswers = null, token) {
    var questions = {
      title: title,
      text: text,
      image: image,
      possibleAnswers: possibleAnswers
    }
    return this.call("post", "/questions", questions, token)
  },
  putUpdateQuestion(id, title = null, text = null, image = null, possibleAnswers = null, token) {
    var questions = {
      title: title,
      text: text,
      image: image,
      possibleAnswers: possibleAnswers
    }
    return this.call("post", "/questions" + id, questions, token)
  },
  delQuestion(token, id) {
    return this.call("delete", "questions/" + id, null, token)
  },
  delAllQuestion(token) {
    return this.call("delete", "questions/all", null, token)
  },
  delAllParticipations(token) {
    return this.call("delete", "questions/participations/all", null, token)
  }
};