<template>
  <q-page class="">
    <tabs-conteiner
      :nav_route="false"
      :tabs="false"
      :component_lists="component_lists"
      :current_component="current_component"
    >
      <div class="text-body1 q-px-lg column items-center">
        <div style="max-width: 1200px">
          <q-banner inline-actions class="text-white q-my-md bg-red">
            Cтраница находится на стадии разработки. Ниже описан будущий
            функционал.
          </q-banner>
          <q-form @submit.prevent="handleSubmit" class="q-my-lg">
            <q-input
              v-model="name"
              label="Имя"
              placeholder="Введите ваше имя"
              type="text"
              :disable="authStore.user ? true : false"
              required
            />
            <q-input
              v-model="email"
              label="Email"
              placeholder="Введите ваш email"
              type="email"
              :disable="authStore.user ? true : false"
              required
            />
            <q-input
              v-model="subject"
              label="Тема"
              placeholder="Введите тему сообщения"
              type="text"
              required
            />
            <q-input
              v-model="message"
              label="Сообщение"
              placeholder="Введите ваше сообщение"
              type="textarea"
              required
            />
            <q-btn
              label="Отправить"
              class="q-my-lg"
              type="submit"
              color="primary"
            />
          </q-form>
        </div>
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { useMeta } from "quasar";
import { setBreadscrumbs } from "src/services/Service";
import { ref, onMounted } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useAuthStore } from "src/stores/all";

const authStore = useAuthStore();

const name = ref("");
const email = ref("");
const subject = ref("");
const message = ref("");

const handleSubmit = () => {
  // Здесь должна быть логика для отправки формы на сервер
  // например, используя библиотеку axios
};

const current_component = ref("show");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "show", // Имя файла компонента
    title: "Написать нам", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value = "Обратная связь";
  updateBreadscrumbs("Обратная связь");

  if (authStore.user) {
    name.value = authStore.user.username;
    email.value = authStore.user.email;
  }
});

const updateBreadscrumbs = (title) => {
  setBreadscrumbs(
    [
      {
        path: "/about",
        meta: { title: "О нас" },
      },
    ],
    title,
    true
  );
};

useMeta(() => {
  return {
    title: meta_title.value + " : Усадьба Мечты",
  };
});
</script>

<style lang="scss" scoped>
.my-card {
  width: 100%;
  max-width: 250px;
}
</style>
