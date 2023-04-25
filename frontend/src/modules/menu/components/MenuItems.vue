<template>
  <div>
    <ul v-if="menu">
      <li v-for="item in menu_root()" :key="item.id">
        <span>{{ item.name }}</span>
        <ul>
          <li v-for="i in sub_menu(item.id)" :key="i.id">
            {{ i.name }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { useMenuStore } from "../store";
import { useRoute, useRouter } from "vue-router";

const menuStore = useMenuStore();
const menu = ref(null);

onMounted(async () => {
  await menuStore.loadMenuItems();
  menu.value = menuStore.menu_items;
});

const sub_menu = (id) => {
  if(menu.value){
    return menu.value.filter((child) => child.parent_id === id);
  }
};
const menu_root = () => {
  if(menu.value){
    return menu.value.filter((child) => child.parent_id === 0);
  }
};
</script>

<style lang="scss" scoped></style>
