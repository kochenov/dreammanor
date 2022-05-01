<template>
  <div class="page wrap">
    <main class="page-main home">
      <TabsWrap
        :current-component="isComponent"
        :tabs="true"
        :box-components="componens"
        @setCurrentComponent="
          (c) => {
            isComponent = c;
          }
        "
      >
        <component :is="isComponent" />
      </TabsWrap>
    </main>
    <aside class="sidebar">
      <div class="box">
        <TabsWrap
          v-if="isComponent === 'FormSeeding'"
          :box-components="[
            {
              title: 'Овощи для расчётов',
              flag: '',
            },
          ]"
        >
          <ListVegetable
            @setVegetableId="
              (e) => {
                setVegetableId(e);
              }
            "
            :data="vegetables"
            :currentID="vegetableId"
          />
          {{ test }}
        </TabsWrap>
        <TabsWrap
          v-if="isComponent === 'HistorySeeding'"
          :box-components="[
            {
              title: 'Фильтр по овощам',
              flag: '',
            },
          ]"
        >
          <ListVegetable
            @setVegetableId="
              (e) => {
                setVegetableId(e);
              }
            "
            :data="vegetables"
            :currentID="vegetableId"
          />
          {{ test }}
        </TabsWrap>
      </div>
    </aside>
  </div>
</template>

<script>
import TabsWrap from "@/components/block/blockTabs/TabsWrap.vue";
import FormSeeding from "@/components/parts/seeding/FormSeeding.vue";
import HistorySeeding from "@/components/parts/seeding/HistorySeeding.vue";
import UserSeeding from "@/components/parts/seeding/UserSeeding.vue";
import ListVegetable from "@/components/block/sidebar/ListVegetable.vue";
import { mapActions, mapGetters, mapMutations, mapState } from "vuex";

export default {
  name: "SeedingPage",
  components: {
    TabsWrap,
    FormSeeding,
    HistorySeeding,
    UserSeeding,
    ListVegetable,
  },
  computed: {
    ...mapState({
      vegetableId: (state) => state.seeding.vegetableId,
      vegetables: (state) => state.seeding.vegetables,
    }),
    ...mapGetters({
      //vegetable: "getVegetable",
    }),
  },
  data() {
    return {
      isComponent: "FormSeeding",
      test: "",
      componens: [
        {
          nameComponent: "FormSeeding",
          title: "Калькулятор размера грядок",
          menu: "Расчёт",
          flag: "",
        },
        {
          nameComponent: "HistorySeeding",
          title: "История рассчётов",
          menu: "История",
          flag: "box-new",
        },
        {
          nameComponent: "UserSeeding",
          title: "Мои посадки",
          menu: "Мои посадки",
          flag: "box-popular",
        },
      ],
    };
  },
  methods: {
    ...mapActions({
      loadVegetables: "loadVegetables",
    }),
    ...mapMutations({
      setVegetableId: "setVegetableId",
    }),
  },
  mounted() {
    //this.vegetables.length == 0 ? this.loadVegetables() : null;
    this.loadVegetables();
  },
};
</script>

<style lang="scss" scoped></style>
