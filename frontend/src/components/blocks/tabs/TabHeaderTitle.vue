!
<template>
  <q-item-section style="flex: 1 1 auto">
    <q-item-label
      ><h1 class="text-h6 title">{{ title }}</h1></q-item-label
    >
    <q-item-label v-if="sub_title" caption>
      {{ sub_title }}
    </q-item-label>
  </q-item-section>
  <tab-menu-component
    v-if="!nav_route && tabs"
    :component_lists="component_lists"
    :current_component="current_component"
    @setCurComponent="
      (c) => {
        $emit('currentComponent', c);
      }
    "
  />
  <tab-menu-route v-if="nav_route && tabs" :component_lists="component_lists" />
</template>

<script setup>
import { computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useNavigationsStore } from "stores/navigations";
import { useMeta } from "quasar";
import TabMenuComponent from "./TabMenuComponent.vue";
import TabMenuRoute from "./TabMenuRoute.vue";

const navigations = useNavigationsStore();
const route = useRoute();
const router = useRouter();
const emit = defineEmits(["currentComponent"]);
const props = defineProps({
  tabs: { Boolean, default: false },
  nav_route: { Boolean, default: true },
  component_lists: { Array },
  current_component: { String },
});

const sub_title = computed(() => {
  return getSubTitle();
});
const title = computed(() => {
  return getTitle();
});

// Сравнивает slug? с алиасом компонента, если ок, возвращает заголовок
// Если нет, то 404
const getTitle = () => {
  let component = null;
  if (props.nav_route) {
    component = props.component_lists.find(
      (o) => o.name_component.toLowerCase() === route.params.id_component
    );
  } else {
    component = props.component_lists.find((o) => {
      if (o.name_component === props.current_component) {
        return true;
      }
    });
  }
  if (route.params.id_component === "") {
    router.push({ path: props.component_lists[0].to });
  }
  if (component) {
    if (props.nav_route) {
      emit("currentComponent", component.name_component);
      //navigations.current_title = component.title;
    }
    return component.title;
  } else {
    if (props.nav_route) {
      if (
        route.params.id_component !== "" &&
        typeof route.params.id_component != "undefined"
      ) {
        router.replace({ path: "/404" });
      }
    }
  }
};

const getSubTitle = () => {
  let component = null;
  if (props.nav_route) {
    component = props.component_lists.find(
      (o) => o.name_component.toLowerCase() === route.params.id_component
    );
  } else {
    component = props.component_lists.find((o) => {
      if (o.name_component === props.current_component) {
        return true;
      }
    });
  }

  if (component) {
    return component.sub_title;
  }

  return null;
};
</script>

<style lang="scss" scoped>
.title {
  margin: 0;
  padding: 0;
  @media (max-width: $breakpoint-xs-max) {
    font-size: 15px;
  }
}
.start {
  justify-content: start !important;
}
</style>
