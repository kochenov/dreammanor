<template>
  <div class="page wrap">
    <main class="page-main">
      <TabsWrap
        :box-components="[
          {
            title: 'Вход в личный кабинет / Авторизация',
            flag: '',
          },
        ]"
      >
        <FormGrid>
          <RowInput>
            <InputForm
              idLabel="username"
              :modelValue="username"
              placeholder="Введите имя пользователя"
              @update:modelValue="(e) => (username = e)"
            />
            <InputForm
              idLabel="password"
              :modelValue="password"
              placeholder="Введите пароль"
              @update:modelValue="(e) => (password = e)"
            />
            <ButtonExp @click.prevent="login(username, password)">
              ВОЙТИ
            </ButtonExp>
          </RowInput>
        </FormGrid>
      </TabsWrap>
    </main>
    <aside class="sidebar"></aside>
  </div>
</template>

<script>
import FormGrid from "@/components/ui/form/FormGrid.vue";
import InputForm from "@/components/ui/form/InputForm.vue";
import RowInput from "@/components/ui/form/RowInput.vue";
import ButtonExp from "@/components/ui/ButtonExp.vue";
import TabsWrap from "@/components/block/blockTabs/TabsWrap.vue";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    ...mapActions({
      //loginStatus: "login",
    }),
    login(username, password) {
      console.log(username, password);
      //this.loginStatus(this.login, this.password);
    },
  },
  components: { FormGrid, InputForm, RowInput, ButtonExp, TabsWrap },
};
</script>

<style lang="scss" scoped></style>
