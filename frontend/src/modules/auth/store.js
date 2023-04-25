import { defineStore } from "pinia";
//import { getError } from "../utils/helpers";
import AuthService from "./authService";
//import { useUserStore } from "stores/all";
import { Notify } from "quasar";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    user: null,
    currentRoute: null,
    error: null,
    loading: false,
  }),

  actions: {
    async login(payload) {
      try {
        return await AuthService.login(payload);
      } catch (error) {
        console.log(error);
        Notify.create({ message: error.code });
      }
    },
    async logout() {
      try {
        let res = await AuthService.logout();
        if (res.status == 200) {
          this.user = null;
        }
      } catch (error) {
        this.user = null;
        console.log(error);
        //this.error = error;
      }
    },
    // Получение текущего пользователя
    async getAuthUser() {
      try {
        // Устанавливаю флаг загрузки на активный
        this.loading = true;
        //
        this.user = await AuthService.getAuthUser();

        this.loading = false;
      } catch (error) {
        // обнуляю данные
        this.user = null;
        // флаг загрузки
        this.loading = false;
        // вывод ошибки
        this.error = error;
      }
    },
    async registration(payload) {
      try {
        //const userStore = useUserStore();
        const userCreditals = await AuthService.registerUser(payload);
        //await userStore.createUser(this.user.uid, payload);
        Notify.create({
          message: "Вы успешно зарегистрировались! Теперь можно войти на сайт",
          color: "green",
        });
        this.router.push({ path: "/login" });
      } catch (error) {
        if (error.response.data.detail == "REGISTER_USER_ALREADY_EXISTS") {
          Notify.create({
            message: "Пользователь с такими данными уже зарегистрирован",
            color: "red",
          });
        }
        //Notify.create({ message: error.code });
      }
    },
    async resetPassword(email) {
      try {
        const status = await AuthService.resetPassword(email);
        Notify.create({
          message: "Для восстановления аккаунта проверте ваш почтовый ящик",
        });
      } catch (error) {
        Notify.create({ message: error.code });
      }
    },
  },

  getters: {
    loggedIn: (state) => !!state.user,
    isAdmin: (state) => (state.user ? state.user.isAdmin : false),
  },
});
