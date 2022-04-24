<template>
  <div class="calc-seeding">
    <FleshMesseges :messages="messages" />
    <FleshMesseges
      v-if="!errorDataApi"
      :messages="[
        'Не удалось получить данные с сервера! Проверьте интернет соединение...',
      ]"
    />
    <FormGrid>
      <RowInput>
        <SelectForm
          :modelValue="currentSort"
          @update:modelValue="(e) => (currentSort = e)"
          :options="sorts"
          name="Выбирите сорт томата"
          idLabel="sort-tomat"
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
          @update:modelValue="(e) => (bushes = e)"
        />
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Количество рядов"
          idLabel="rows"
          :modelValue="rows"
          @update:modelValue="(e) => (rows = e)"
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
          @update:modelValue="(e) => (distanceBetweenRows = e)"
        />
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Расстояние между кустов, см"
          idLabel="distanceBetweenBushes"
          :modelValue="distanceBetweenBushes"
          @update:modelValue="(e) => (distanceBetweenBushes = e)"
        />
      </RowInput>
      <BrnGroup>
        <ButtonExp @click.prevent=""> Сделать расчёт </ButtonExp>
      </BrnGroup>
    </FormGrid>
    {{ currentSort }}
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

export default {
  name: "FormSeeding",
  data() {
    return {
      messages: [],
      errorDataApi: false,
      loadingDataApi: true,
      currentSort: "default",
      distanceBetweenRows: "50",
      distanceBetweenBushes: "70",
      bushes: "1",
      rows: "1",
      sorts: [
        { id: "1", name: "Sort 1" },
        { id: "2", name: "Sort 2" },
      ],
    };
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
  },
};
</script>

<style lang="scss" scoped></style>
