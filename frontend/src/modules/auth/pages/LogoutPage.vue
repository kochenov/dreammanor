<template>
  <div><q-spinner-hourglass color="purple" size="4em" /></div>
</template>
<script setup>
import { useAuthStore } from "../store";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const route = useRouter();

const logout = async () => {
  await authStore.logout();
  if (authStore.currentRoute) {
    route.push(authStore.currentRoute);
    authStore.currentRoute = null;
    authStore.error = null;
  }
};

logout();
</script>
