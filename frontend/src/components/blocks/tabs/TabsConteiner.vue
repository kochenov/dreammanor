<template>
  <div class="box q-my-lg q-mx-xs">
    <q-card class="my-card" flat bordered>
      <q-item>
        <!--TAB HEDER TITLE-->
        <tab-header-title
          :tabs="tabs"
          :component_lists="component_lists"
          :nav_route="nav_route"
          :current_component="current_component"
          @currentComponent="
            (c) => {
              $emit('setCurrentComponent', c);
            }
          "
        />
        <!--TABS MENU -->
      </q-item>

      <q-separator />

      <q-card-section>
        <slot />
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>
import TabHeaderTitle from "./TabHeaderTitle.vue";

const props = defineProps({
  tabs: { type: Boolean, default: false },
  nav_route: { type: Boolean, default: true },
  current_component: { type: String },
  //base_route: { type: String, default: "" },
  component_lists: {
    type: Array,
    default() {
      return [
        /*  {
          name_component: "FormSeeding", // Имя файла компонента
          title: "Заголовок страницы", // Заголовок текущего компонента
          to: "/slug1/slug2",
          text_btn: "Расчёт", // Имя вкладки
          flag: "", // Флаг блока {'box-new' / 'box-popular' }
        }, */
      ];
    },
    require: true,
  },
});
</script>

<style lang="scss" scoped></style>
