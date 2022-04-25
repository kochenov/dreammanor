<template>
  <ul class="list-menu-link">
    <li
      v-for="item in data"
      :key="item.id"
      :class="{ active: item.id == currentID }"
    >
      <a @click.prevent="$emit('setVegetableId', item.id)" href="#">{{
        item.name
      }}</a>
    </li>
  </ul>
</template>

<script>
export default {
  name: "ListVegetable",
  props: {
    data: {
      type: Array,
      default: () => {
        return [];
      },
    },
    currentID: {
      type: [String, Number],
    },
  },
};
</script>

<style lang="scss" scoped>
.list-menu-link {
  margin-left: 40px;
  list-style: none;

  li {
    margin-bottom: 8px;
    font-weight: 600;

    &::before {
      content: url("~@/assets/images/icons/i-list.svg");
      // background-image: url(/img/icons/i-list.svg);
      transform: scale(2);
      height: auto;
      width: 3px;
      display: inline-block;
      //background-size: 8px;
      //background-repeat: no-repeat;
      padding-right: 10px !important;
    }

    &:hover::before {
      content: url("~@/assets/images/icons/i-list-hover.svg");
    }

    &:hover,
    a:hover {
      color: #06b25f;
    }
  }

  .active {
    &::before {
      content: url("~@/assets/images/icons/i-list-hover.svg");
    }

    a {
      color: #06b25f;
      fill: #06b25f;
    }
  }

  a {
    font-size: 14px;
    text-decoration: none;
    color: #000;
  }
}
</style>
