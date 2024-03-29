import { boot } from "quasar/wrappers";
import { useAuthStore } from "stores/all";
import { ref } from "vue";

export default boot(async ({ router }) => {
  // Маршруты для гостей
  const guestAuthRoutes = [
    "login",
    "registration",
    "forgotPassword",
    "passwordReset",
  ];

  router.beforeEach(async (to, from) => {
    const authStore = useAuthStore();

    if (
      to.fullPath == "/login" ||
      to.fullPath == "/registration" ||
      to.fullPath == "/logout"
    ) {
      authStore.currentRoute = from.fullPath;
    }

    // получить текущего пользователя
    await authStore.getAuthUser();

    if (authStore.user && authStore.user.id == 1) {
      //console.log(authStore.user);
      //const userStore = useUserStore();
    }
    // если страница закрыта для гостей, то переадресует на страницу авторизации
    if (to.meta.auth && !authStore.user) {
      // this route requires auth, check if logged in
      // if not, redirect to login page.
      return {
        path: "/login",
        // save the location we were at to come back later
        query: { redirect: to.fullPath },
      };
    }

    // Переадресует авторизованного пользователя если он зашёл на страницу для гостя
    if (authStore.user && guestAuthRoutes.includes(to.name)) {
      return {
        path: "/",
      };
    }
  });
});
