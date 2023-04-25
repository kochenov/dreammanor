<template>
  <div class="box box-tab">
    <div class="box__header">
      <div class="box__header-wrapper-tabs">
        <h2
          v-for="(item, index) in boxComponents"
          :key="index"
          class="box__header-title"
          :class="[
            tabs ? 'tab-link' : '',
            currentComponent === item.nameComponent ? 'active' : '',
            item.flag,
          ]"
        >
          {{ item.title }}
        </h2>
      </div>
      <div v-if="tabs" class="box__header-links wrapper-link-tabs">
        <a
          v-for="(item, index) in boxComponents"
          :key="index"
          class="box__header-link"
          :class="{ active: currentComponent === item.nameComponent }"
          href="#"
          @click.prevent="$emit('setCurrentComponent', item.nameComponent)"
          >{{ item.menu }}</a
        >
      </div>
    </div>
    <div class="box__panel">
      <slot />
    </div>
  </div>

  <WrapTabs
    @setCurrentComponent="
      (c) => {
        isComponent = c;
      }
    "
    :tabs="true"
    :current-component="isComponent"
    :box-components="pageComponents"
  >
    {{ isComponent }}
  </WrapTabs>
</template>
<script setup>
import { useRoute } from "vue-router";
const route = useRoute();
const props = defineProps({
  tabs: { type: Boolean, default: false },
  currentComponent: { type: String },
  /**
   * Массив обьектов описывающий вкладки и заголовки компонентов
   *
   * - nameComponent: "FormSeeding", // Имя файла компонента
   * - title: "Заголовок страницы", // Заголовок текущего компонента
   * - menu: "Расчёт", // Имя вкладки
   * - flag: "", // Флаг блока {'box-new' / 'box-popular' }
   *
   */
  boxComponents: {
    type: Array,
    default() {
      return [
        {
          nameComponent: "FormSeeding", // Имя файла компонента
          title: "Заголовок страницы", // Заголовок текущего компонента
          menu: "Расчёт", // Имя вкладки
          flag: "", // Флаг блока {'box-new' / 'box-popular' }
        },
      ];
    },
    require: true,
  },
});
</script>
<style lang="scss" scoped>
.box {
  width: 100%;

  &__header {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(24, 107, 35, 0.315);
    margin-left: 45px;
    margin-right: 45px;
    align-items: center;
    margin-top: 30px;
    font-size: 18rem;
    &-wrapper-tabs {
      .tab-link {
        display: none;
      }

      .active {
        display: block;
      }
    }

    &-title {
      font-family: Bitter;
      font-weight: 400;
      line-height: 0.75rem;
      letter-spacing: 0em;
      position: relative;
      font-size: 24rem;
    }

    &-link-tabs {
      margin-right: 10px;
    }

    &-links {
      .active {
        color: #fff;
        background-color: #06b25f;
        -webkit-transition: 0.5s ease;
        transition: 0.5s ease;
      }
    }

    &-link {
      text-decoration: none;
      color: black;
      border: 1px solid #06b25f;
      font-size: 14rem;
      padding: 5px;
      -webkit-transition: 1s ease;
      transition: 1s ease;
      margin-left: 5px;

      &:hover {
        color: #fff;
        background-color: #06b25f;
        -webkit-transition: 0.5s ease;
        transition: 0.5s ease;
      }
    }

    .box-fresh:before {
      content: "СВЕЖИЕ";
      color: #fff;
      font-size: 11px;
      position: absolute;
      top: 6px;
      left: -47px;
      transform: rotate(-90deg);
      padding: 4px;
      background-color: rgb(231, 14, 14);
      top: 0px;
      left: -70px;
      transform: rotate(0);
    }

    .box-popular:before {
      content: "ВАЖНЫЕ";
      color: #fff;
      font-size: 11px;
      position: absolute;
      top: 5px;
      left: -47px;
      transform: rotate(-90deg);
      padding: 4px;
      padding-left: 3px;
      padding-right: 3px;
      background-color: $green-dark;
      top: 0px;
      left: -70px;
      transform: rotate(0);
    }

    .box-new:before {
      content: "НОВЫЕ";
      color: #fff;
      font-size: 11px;
      position: absolute;
      top: 6px;
      left: -47px;
      transform: rotate(-90deg);
      padding: 4px;
      background-color: rgb(14, 90, 231);
      top: 0px;
      left: -70px;
      transform: rotate(0);
    }
  }

  &__panel {
    padding: 20px 0px 20px 20px;
    position: relative;
    font-size: 14rem;

    height: 100%;
    margin-left: 20px;
    margin-top: 20px;
  }
}

.box {
  &__content {
    padding: 6px;
  }
}

.wrapper-link-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 0px;
  justify-content: center;
}
</style>
