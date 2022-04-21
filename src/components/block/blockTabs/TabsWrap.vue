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
          @click="$emit('setCurrentComponent', item.nameComponent)"
          >{{ item.menu }}</a
        >
      </div>
    </div>
    <div class="box__panel">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tabs: { type: Boolean, default: false },
    /**
     * Имя файла текущего компонента
     */
    currentComponent: {
      type: String,
      default: "",
      require: true,
    },
    /**
     * Список компонентов , см. default()
     */
    boxComponents: {
      type: Array,
      default() {
        return [
          {
            nameComponent: "FormSeeding", // Имя файла компонента
            title: "Калькулятор посева овощей", // Заголовок текущего компонента
            menu: "Расчёт", // Имя вкладки
            flag: "", // Флаг блока {'box-new' / 'box-popular' }
          },
        ];
      },
      require: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.box {
  width: 100%;

  &__header {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(24, 107, 35, 0.315);
    padding-bottom: 10px;
    margin-left: 45px;
    align-items: center;
    margin-top: 30px;
    @include screen-size(xl) {
      margin-left: 0;
    }
    @include screen-size(lg) {
      font-size: 18rem;
      flex-direction: column-reverse;
      gap: 30px;
    }

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
      font-size: 30rem;
      letter-spacing: 0em;
      position: relative;
      @include screen-size(xl) {
        font-size: 24rem;
      }
      @include screen-size(lg) {
        font-size: 18rem;
      }
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
      @include screen-size(xl) {
        font-size: 12rem;
      }
      @include screen-size(lg) {
        font-size: 16rem;
      }

      &:hover {
        color: #fff;
        background-color: #06b25f;
        -webkit-transition: 0.5s ease;
        transition: 0.5s ease;
      }
    }

    @mixin box() {
      @include screen-size(lg) {
        top: 0px;
        left: -70px;
        transform: rotate(0);
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
      @include box();
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
      @include box();
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
      @include box();
    }
  }

  &__panel {
    padding: 20px;
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
</style>
