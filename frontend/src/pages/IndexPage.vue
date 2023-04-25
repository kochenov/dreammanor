<template>
  <q-page class="">
    <tabs-conteiner
      :component_lists="component_lists"
      :current_component="current_component"
      :nav_route="false"
    >
      <div class="q-pa-sm row q-col-gutter-lg" >
        <div class="col-sm-6 col-12">
          <h2 class="text-h6">Сайт находится в разработке</h2>
          <q-separator  class="q-mb-lg"/>
          <q-form @submit.prevent="onSubmit" class="q-pt-sm q-gutter-xl">
            <q-input
              outlined
              v-model="numberObj"
              label="Номер объекта недвижимости*"
              hint="Номер дома из видео"
              type="number"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) || 'Пожалуйста введите номер объекта',
                  (val) => !isNaN(parseInt(val)) || 'Нужно вводить число',
              ]"
            />

            <div>
              <q-btn label="Начать поиск" type="submit" color="primary" />
            </div>
          </q-form>

        </div>
        <div class="col">
          <h2 class="text-h6">Сайт находится в разработке</h2>
          <div class="text-body1">
            <p>
              Ни для кого не секрет, что сейчас в интернете можно найти
              практически любую информацию. Однако, не все сайты доступны для
              посещения в любое время. Именно таким является сайт, находящийся в
              стадии разработки и пока не доступный для всех пользователей.
            </p>
            <p>
              На данный момент, основной функционал сайта состоит из
              видеообзоров и объявлений о продаже недвижимости. Однако, из-за
              того, что сайт находится в разработке, некоторые страницы могут
              быть недоступны или не работать корректно.
            </p>
            <p>
              Несмотря на это, разработчики продолжают работу над улучшением
              функционала и скоро сайт станет доступным для всех пользователей.
              Ведь главная цель разработки сайта – предоставить пользователю
              максимум полезной и актуальной информации в удобном формате.
            </p>
            <p>
              Если вы заинтересованы в видеообзорах и планируете купить
              недвижимость, то данный сайт может стать полезным для вас. Следите
              за обновлениями и не пропустите момент, когда сайт станет доступен
              для всех пользователей!
            </p>
          </div>
        </div>
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useNavigationsStore } from "src/stores/navigations";
import {useEstateStore} from "src/stores/all"
import { useRoute, useRouter } from "vue-router";

const numberObj = ref(null);
const navigations = useNavigationsStore();
const realEstateStore = useEstateStore();
const route = useRouter();

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
const onSubmit = async () => {
  // по номеру объекта (UIN) найти недвижимость в базе
  // если недвижимость есть, сделать hgthtflhtcfwb. на страницу
  let res = await realEstateStore.findHome(numberObj.value);
  if(res){
    route.push(`/desk/realEstate/home/${res.id}`)
  }else{
    // Если недвижимости нет, найти в базе с номером объявление и переадресовать на страницу авито
    let res_link = await realEstateStore.findLink(numberObj.value);
    if(res_link){
      window.open(res_link.link, '_blank');
    }else{
      // если в БД нет ни одной записи, показать сообщение, что данных нет
      Notify.create({
            message: `Объяъект недвижимости с номером [${numberObj.value}] не неаден`,
            color: "red",
          });
    }
  }



 };
navigations.current_title = "Форма поиска дома по номеру объекта";
</script>
