<template>
  <div class="calc-seeding">
    <FleshMesseges :messages="messages" />
    <FleshMesseges
      v-if="errorDataApi"
      :messages="[
        'Не удалось получить данные с сервера! Проверьте интернет соединение...',
      ]"
    />
    <FormGrid>
      <RowInput>
        <SelectForm
          :modelValue="currentSort"
          @update:modelValue="(e) => loadDataSorts(e)"
          :options="sorts"
          :name="'Выберите сорт овоща, ' + vegetable.name"
          idLabel="sort"
        >
          <SelectOptionForm selected disabled value="default"
            >Сорт не выбран</SelectOptionForm
          >
        </SelectForm>

        <InputForm
          typeInput="number"
          min="1"
          max="1000"
          placeholder="Введите положительное число от 1 до 1000"
          name="Количество кустов"
          idLabel="bushes"
          :modelValue="bushes"
          @update:modelValue="(e) => (bushes = Number(e))"
        />
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Количество рядов"
          idLabel="rows"
          :modelValue="rows"
          @update:modelValue="(e) => (rows = Number(e))"
        />
      </RowInput>
      <RowInput>
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Расстояние между рядов, см"
          idLabel="distanceBetweenRows"
          :modelValue="distanceBetweenRows"
          @update:modelValue="(e) => (distanceBetweenRows = Number(e))"
        />
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Расстояние между кустов, см"
          idLabel="distanceBetweenBushes"
          :modelValue="distanceBetweenBushes"
          @update:modelValue="(e) => (distanceBetweenBushes = Number(e))"
        />
      </RowInput>
      <BrnGroup>
        <ButtonExp @click.prevent="submitToResult"> Сделать расчёт </ButtonExp>
      </BrnGroup>
    </FormGrid>
    <ResultSeeding
      :bushes="Number(bushes)"
      :distanceBetweenBushes="Number(distanceBetweenBushes)"
      :distanceBetweenRows="Number(distanceBetweenRows)"
      :rows="Number(rows)"
      :active="active"
      v-if="result"
    />
  </div>
</template>

<script>
import FleshMesseges from "@/components/ui/FleshMesseges.vue";
import FormGrid from "../../ui/form/FormGrid.vue";
import RowInput from "@/components/ui/form/RowInput.vue";
import InputForm from "@/components/ui/form/InputForm.vue";
import SelectForm from "@/components/ui/form/SelectForm.vue";
import SelectOptionForm from "@/components/ui/form/SelectOptionForm.vue";
import ButtonExp from "@/components/ui/ButtonExp.vue";
import BrnGroup from "../../ui/Button/BrnGroup.vue";
import { mapState, mapGetters } from "vuex";
import ResultSeeding from "./results/ResultSeeding.vue";

export default {
  name: "FormSeeding",

  data() {
    return {
      messages: [],
      loadingDataApi: true,
      currentSort: "default",
      distanceBetweenRows: "",
      distanceBetweenBushes: "",
      bushes: 1,
      rows: 1,
      active: 1,
      result: false,
    };
  },

  computed: {
    ...mapState({
      errorDataApi: (state) => state.seeding.errorDataApi,
    }),
    ...mapGetters({
      sorts: "getSorts",
      vegetable: "getVegetable",
    }),
  },
  watch: {
    active() {},
  },
  methods: {
    // Стабатывает при выборе сорта из select
    loadDataSorts(id) {
      this.currentSort = id;
      let sort = this.sorts.find((item) => item.id == id);
      this.distanceBetweenRows = sort.distanceBetweenRows;
      this.distanceBetweenBushes = sort.distanceBetweenBushes;
    },
    // Проверяет, что бы все поля были заполнены
    validInputsEmpty() {
      if (
        this.distanceBetweenRows !== "" &&
        this.distanceBetweenBushes !== "" &&
        this.bushes !== "" &&
        this.rows !== ""
      ) {
        this.messages = [];
        return true;
      } else {
        this.messages = ["Пожалуйста, заполните все поля формы!"];
        this.result = false;
        return false;
      }
    },
    // Проверяет, что бы количество кустов небыло меньше количества рядов
    validRowsbushes() {
      if (this.bushes >= this.rows) {
        this.messages = [];
        return true;
      } else {
        this.messages = [
          "Количество рядов не должно превышать количество кустов",
        ];
        this.result = false;
        return false;
      }
    },

    submitToResult() {
      // Проверяем, поля формы. Дожны быть все заполнены
      if (this.validInputsEmpty()) {
        // Если валидация полей прошла, проверяем количество кустов и рядов
        // Должно быть рядов меньше или равно количеству кустов
        if (this.validRowsbushes()) {
          // меняем состояние на нажатое
          this.result = true;

          // Очищаем список ошибок
          this.message = [];
          this.active =
            Number(this.rows) +
            Number(this.bushes) +
            Number(this.distanceBetweenRows) +
            Number(this.distanceBetweenBushes);
        }
      }
    },
  },
  components: {
    FleshMesseges,
    FormGrid,
    RowInput,
    InputForm,
    SelectForm,
    SelectOptionForm,
    ButtonExp,
    BrnGroup,
    ResultSeeding,
  },
};
</script>

<style lang="scss" scoped></style>
