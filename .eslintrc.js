module.exports = {
  root: true,

  env: {
    node: true,
  },

  parserOptions: {
    parser: "@babel/eslint-parser",
  },

  rules: {
    "no-console": "off",
    "no-debugger": "off",
  },

  overrides: [
    {
      files: [
        "**/__tests__/*.{j,t}s?(x)",
        "**/tests/unit/**/*.spec.{j,t}s?(x)",
      ],
      env: {
        jest: true,
      },
    },
  ],

  extends: [
    "plugin:vue/essential",
    "eslint:recommended",
    "plugin:prettier/recommended",
  ],
};
