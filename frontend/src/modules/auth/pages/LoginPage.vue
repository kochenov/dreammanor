<template>
  <q-card class="q-ma-lg">
    <div class="row">
      <div class="col-0 col-sm-5 bg-primary rounded-left-borders xs-hide">
        <div
          class="row full-width q-px-xl q-pb-xl full-height flex flex-center"
        >
          <div class="">
            <div
              class="text-h4 text-uppercase text-white fredoka"
              style="min-width: 220px"
            >
              ДОБРО ПОЖАЛОВАТЬ!
            </div>
            <div class="text-white q-my-sm text-subtitle1">
              Введите свои учетные данные для входа в систему!
            </div>
          </div>
        </div>
      </div>
      <div class="col-12 col-sm-7">
        <div class="row q-ml-sm q-mt-sm sm-and-up-hide">
          <div class="col-12 fredoka text-subtitle1">
            <router-link
              class="text-primary"
              style="text-decoration: none"
              to="/"
            >
              Перейти на главную
            </router-link>
          </div>
        </div>
        <div class="row q-pa-sm-sm q-pa-md">
          <div class="col-12">
            <q-card-section>
              <div class="q-mb-xl">
                <div class="flex justify-center">
                  <div
                    class="text-h4 text-uppercase q-my-none text-weight-bold text-primary fredoka"
                  >
                    Войти
                  </div>
                </div>
              </div>
              <q-form class="q-gutter-md" @submit="onSubmit">
                <q-input
                  v-model="email"
                  label="Введите email"
                  lazy-rules
                  name="email"
                  type="email"
                />
                <q-input
                  v-model="password"
                  label="Пароль"
                  lazy-rules
                  name="password"
                  type="password"
                />
                <div>
                  <q-btn
                    class="full-width fredoka"
                    color="primary"
                    label="Войти"
                    type="submit"
                  ></q-btn>
                  <div class="q-mt-lg">
                    <div class="q-mt-sm">
                      У вас еще нет учетной записи?
                      <router-link class="text-primary" to="/registration"
                        >Регистрация</router-link
                      >
                    </div>
                    <div class="q-mt-sm">
                      Забыли пароль?
                      <router-link class="text-primary" to="/forgot-password"
                        >Нажмите здесь!</router-link
                      >
                    </div>
                  </div>
                </div>
              </q-form>
            </q-card-section>
          </div>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script setup>
import { Notify } from "quasar";
import { useAuthStore } from "src/stores/all";
import { ref } from "vue";
import { useRouter } from "vue-router";

const route = useRouter();
const email = ref(null);
const password = ref(null);
const authStore = useAuthStore();

const onSubmit = async () => {
  try {
    const userCredital = await authStore.login({
      username: email.value,
      password: password.value,
    });

    if (userCredital && userCredital.status == "200") {
      Notify.create("Выполнен успешный вход!");
      if (authStore.currentRoute) {
        route.push(authStore.currentRoute);
        authStore.currentRoute = null;
        authStore.error = null;
      } else if (route.currentRoute.value.query.redirect) {
        route.push(route.currentRoute.value.query.redirect);
      }
    }
  } catch (error) {
    console.log(error);
  }
};
</script>

<style lang="scss" scoped></style>
