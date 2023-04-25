<template>
  <q-page class="">
    <tabs-conteiner
      :nav_route="false"
      :tabs="false"
      :component_lists="component_lists"
      :current_component="current_component"
    >
      <div class="text-body1 q-px-lg q-mt-lg column items-center">
        <div style="max-width: 1200px">
          <p>
            Приветствуем вас на нашем деревенском портале <b>Усадьба Мечты</b>!
            Чтобы создать уютное и безопасное место для всех пользователей, мы
            установили следующие правила:
          </p>
          <ol class="text-weight-regular q-my-sm q-pl-lg">
            <li>
              Уважайте других пользователей. Никакого оскорбительного или
              дискриминационного поведения не будет допущено. Запрещено
              использование нецензурной лексики или угрожающего поведения.
            </li>
            <li>
              Не публикуйте нелегальный контент. На нашем портале запрещено
              размещать контент, нарушающий законы или права других лиц, такие
              как пиратство, насилие, порнография и т.д.
            </li>
            <li>
              Будьте осторожны с личной информацией. Не сообщайте свой личный
              адрес, номер телефона, данные банковской карты и другую
              конфиденциальную информацию в открытых сообщениях или
              комментариях.
            </li>
            <li>
              Соблюдайте авторские права. Если вы хотите поделиться материалом,
              убедитесь, что у вас есть на это право или что вы дали должные
              ссылки на источник.
            </li>
            <li>
              Не злоупотребляйте возможностями портала. Не размещайте
              спам-рекламу или несанкционированные рекламные сообщения. Не
              злоупотребляйте возможностью приглашать пользователей на другие
              ресурсы.
            </li>
          </ol>
          <p>
            Нарушение любого из вышеуказанных правил может привести к удалению
            материала, временной или постоянной блокировке аккаунта пользователя
            или другим мерам, принятым администрацией сайта. Будьте вежливы и
            уважительны друг к другу, и мы будем иметь приятный и безопасный
            опыт взаимодействия в нашей социальной сети.
          </p>
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

const current_component = ref("show");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "show", // Имя файла компонента
    title: "Правила сайта", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value =
    "Наша команда разработчиков установила следующие правила для сайта ";
  updateBreadscrumbs("Правила");
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
