<template>
  <div class="column">
    <div class="q-py-md row justify-center">
      <div style="width: 100%; max-width: 800px">
        <q-chat-message
          :text="['Have you seen Quasar?']"
          :text-color="i.id % 2 != 0 ? '' : 'white'"
          :bg-color="i.id % 2 != 0 ? 'amber-7' : 'primary'"
          v-for="i in [
            { id: 1 },
            { id: 2 },
            { id: 3 },
            { id: 4 },
            { id: 5 },
            { id: 6 },
            { id: 7 },
            { id: 8 },
            { id: 9 },
            { id: 10 },
          ]"
          :key="i"
        >
          <template v-slot:name>me</template>
          <template v-slot:stamp>
            <div>7 minutes ago</div>
            <div v-if="i.id % 2 == 0" class="row q-mt-md">
              <div class="">
                <span class="pointer" @click="toFormComment()">Ответить </span>
              </div>
            </div>
          </template>
          <template v-slot:avatar>
            <span @click="$router.push('/')">
              <img
                class="q-message-avatar q-mr-md q-message-avatar--sent"
                src="https://cdn.quasar.dev/img/avatar4.jpg"
              />
            </span>
          </template>
        </q-chat-message>
      </div>
    </div>
    <h6 class="text-h6 q-mb-none">Оставить коментарий</h6>
    <q-separator class="q-mb-md" />
    <div>
      <q-editor
        v-model="editor"
        :toolbar="[['bold', 'italic', 'strike', 'underline']]"
      />
      <div class="flex flex-center q-my-md" ref="scrollAreaRef">
        <q-btn color="primary" icon-right="send" label="ДОБАВИТЬ КОМЕНТАРИЙ" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { scroll } from "quasar";
import { useRoute } from "vue-router";
import { useArticlesStore } from "src/stores/all";
const articlesStore = useArticlesStore();

const route = useRoute();
const { setVerticalScrollPosition, getScrollTarget } = scroll;

const scrollAreaRef = ref(null);

const editor = ref("");
const showing = ref(false);

const toFormComment = () => {
  const target = getScrollTarget(scrollAreaRef.value);
  const offset = scrollAreaRef.value.offsetTop;
  setVerticalScrollPosition(target, offset, 300);
};

onMounted(async () => {
  await articlesStore.loadComments(route.params.num);
});
</script>

<style lang="scss" scoped></style>
