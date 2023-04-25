<template>
  <q-tabs
    dense
    inline-label
    align="left"
    shrink
    outside-arrows
    mobile-arrows
    narrow-indicator
    class="main-menu text-primary text-weight-bold gt-sm"
    v-model="tab"
    v-if="mobile == false"
  >
    <q-tab
      v-for="item in menuItems"
      :key="item.id"
      :name="item.name"
      :icon="item.icon"
      :label="item.label"
    />
  </q-tabs>
  <template v-if="mobile">
    <q-item
      @click="mobileTab(item.name)"
      clickable
      v-ripple
      v-for="item in menuItems"
      :key="item.id"
      :active="$route.matched[0].name == item.name"
      active-class="bg-grey-4 text-grey-10"
      class="q-pl-lg"
    >
      <q-item-section>{{
        item.label != null ? item.label : "Главная"
      }}</q-item-section>
      <q-item-section avatar>
        <q-icon color="primary" :name="item.icon" />
      </q-item-section>
    </q-item>
  </template>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const tab = ref("");
const props = defineProps({ mobile: { type: Boolean, default: false } });
const menuItems = [
  {
    id: 1,
    name: "home",
    icon: "home",
    label: null,
  },
  {
    id: 2,
    name: "news",
    icon: "newspaper",
    label: "Новости",
  },
  {
    id: 3,
    name: "about",
    icon: "business",
    label: "О нас",
  },
  {
    id: 4,
    name: "desk",
    icon: "real_estate_agent",
    label: "Объявления",
  },
  {
    id: 5,
    name: "blogs",
    icon: "rss_feed",
    label: "Блоги",
  },
  {
    id: 6,
    name: "articles",
    icon: "feed",
    label: "Статьи",
  },
  {
    id: 7,
    name: "calculate",
    icon: "calculate",
    label: "Расчёты",
  },
  {
    id: 8,
    name: "calendars",
    icon: "calendar_month",
    label: "Календари",
  },
];
onMounted(() => {
  tab.value = route.matched[0].name || "home";
});
const emit = defineEmits(["subMenu", "subMenuMobile"]);
watch(tab, (newValue, oldValue) => {
  emit("subMenu", tab.value);
});
const mobileTab = (name) => {
  tab.value = name;
  emit("subMenuMobile", tab.value);
};
</script>

<style lang="scss">
.main-menu {
  .q-tab__label {
    font-family: "Bitter", sans-serif;
    font-weight: 600;
    font-size: 12px;
    color: #194484;
  }
  .q-tab__icon {
    font-size: 14px;
  }
  .q-tab--inactive {
    opacity: 1;
  }
  .absolute-bottom {
    right: 0;
    bottom: 0px;
    left: 0;
  }
  .q-tab {
    min-height: 50px !important;
  }
  .q-tab__indicator {
    height: 0px;
  }
  .q-tab__indicator::after {
    content: "";
    position: absolute;
    bottom: 0px;
    left: 50%;
    transform: translate(-50%, 0px);
    border-width: 8px;
    border-style: solid;
    border-top-color: transparent;
    border-right-color: transparent;
    border-left-color: transparent;
    border-image: initial;
    border-bottom-color: #194484;
  }
  .q-hoverable:hover {
    .q-focus-helper {
      opacity: 0 !important;
    }
    &::after {
      content: "";
      position: absolute;
      bottom: 0px;
      left: 50%;
      transform: translate(-50%, 0px);
      border-width: 8px;
      border-style: solid;
      border-top-color: transparent;
      border-right-color: transparent;
      border-left-color: transparent;
      border-image: initial;
      border-bottom-color: #194484;
    }
  }
}
</style>
