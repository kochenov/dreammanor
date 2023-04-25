<template>
  <q-page class="">
    <tabs-conteiner
      :component_lists="component_lists"
      :current_component="current_component"
      :nav_route="false"
    >
      <div class="q-pa-sm" style="max-width: 400px">
        <q-form @submit.prevent="onSubmit" class="q-gutter-xl">
          <q-input
            outlined
            v-model="numberObj"
            label="Номер объекта недвижимости*"
            hint="Номер дома из видео"
            lazy-rules
            :rules="[
              (val) =>
                (val && val.length > 0) || 'Пожалуйста введите номер объекта',
            ]"
          />

          <div>
            <q-btn label="Начать поиск" type="submit" color="primary" />
          </div>
        </q-form>
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useNavigationsStore } from "src/stores/navigations";
const numberObj = ref(null);
const navigations = useNavigationsStore();

const current_component = ref("formFind");
const component_lists = [
  {
    name_component: "formFind", // Имя файла компонента
    title: "Найти дом в деревне по номеру объекта", // Заголовок текущего компонента
    sub_title:
      "Найти объявление о продаже дома в деревне по номеру объяета недвижимости из видео",
    text_btn: "", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/formFind",
  },
];
const onSubmit = () => {};
navigations.current_title = "Форма поиска дома по номеру объекта";
</script>
