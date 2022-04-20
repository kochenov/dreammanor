<template>
  <ul class="list-menu-link">
    <li class="active"><a href="#">Посев томатов </a></li>
    <li><a href="#">Посев Огурцов</a></li>
    <li><a href="#">Посев перцев</a></li>
    <li><a href="#">Посев баклажанов</a></li>
    <li><a href="#">Посев кабачков</a></li>
    <li><a href="#">Посев тыквы</a></li>
    <li><a href="#">Посев моркови</a></li>
    <li><a href="#">Посев редиса</a></li>
    <li><a href="#">Посев свеклы</a></li>
    <li><a href="#">Посев капусты</a></li>
    <li><a href="#">Посев арбузов</a></li>
    <li><a href="#">Посев картофеля</a></li>
  </ul>
</template>

<script>
export default {
  name: "ListVegetable",
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
