import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
// Импорт иконок
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import axios from "axios";
import VueAxios from "vue-axios";

library.add(fas);

const app = createApp(App);

app
  .use(store)
  .use(router)
  .use(VueAxios, axios)
  .component("fa", FontAwesomeIcon)
  .mount("#app");
