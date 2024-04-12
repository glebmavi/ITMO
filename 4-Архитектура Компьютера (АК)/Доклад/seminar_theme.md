Я собираюсь сделать доклад. Напиши по шаблону описание доклада используя информацию о теме:
## Шаблон:
<Название доклада отдельной строкой>

<Описание доклада одним абзацем>

<Полезное для слушателей, нумерованным списком>

<Источники информации для подготовки к докладу>

<Вопрос к экзамену>

## Требования:

- Объём описания -- не более 1536 символов.
- Между абзацами необходимо оставлять пустую строку.
- **Название доклада**. Должно быть конкретным и достаточным, чтобы увидеть "дубль" темы в рамках группы. Не должно содержать риторических вопросов.
- **Описание доклада**. Должно сформировать понимание того, о чём вы хотите сделать доклад. Будьте конкретны, избегайте лишних слов, метафор и пространных рассуждений на тему. Если какое-то слово из описания можно убрать, не изменив смысл -- уберите.
- **Полезное для слушателей**. Оформите в виде списка какие полезные знания вы донесёте до слушателей.
    - К примеру, названия конкретных подходов к разработке, контролю качества, инструменты, методы и практики.
    - Историческая справка, детали старых уязвимостей и ошибок, "прописные истины" полезными для слушателей не являются.
- **Вопрос к экзамену**. Так как доклад представляет пользу для учащихся, вам необходимо предложить вопрос на проверку освоения материала. Требования к вопросу:
    - Знание ответа на ваш вопрос должно быть полезно для студента в современных реалиях. Оно должно быть связано с разработкой и устройством компьютерных систем.
    - Ответ на вопрос должен занимать примерно пару минут содержательной речи.
    - Вопрос должен иметь закрытую формулировку. К примеру:
        - Плохо: "Расскажите о методах тестирования ПО?".
        - Хорошо: "Методы оценки качества тестового покрытия. Test coverage и другие метрики."
    - Вопрос должен наводить учащегося на правильный ответ. К примеру:
        - Плохо: "В чём заключается механизм ошибки ED-4312?"
        - Хорошо: "Как работает механизм переполнения буфера в рамках ED-4312?"
        - Плохо: "Перечислите все уязвимости проекта X."
        - Хорошо: "В проекте X присутствовали следующие уязвимости: ... Опишите механизм их использования для атаки?"

## Информация для доклада:
Эта информация взята из разных источников.

Model Quantization is a technique used to reduce the size of large neural networks, including large language models (LLMs) by modifying the precision of their weights. LLM Quantization is enabled thanks to empiric results showing that while some operations related to neural network training and inference must leverage high precision, in some cases it's possible to use significantly lower precision (float16 for example) reducing the overall size of the model, allowing it to be run using less powerful hardware with an acceptable reduction of its capabilities and accuracy. In this blog post I will go over the LLM Quantization and cover following points:

    Basics of quantization

    Advantages and disadvantages of quantized models 

    Find and use already quantized models

    Quantization techniques including sample code


Large Language Models (LLMs) are known for their extensive computational requirements. Typically, the size of a model is calculated by multiplying the number of parameters (size) by the precision of these values (data type). However, to save memory, weights can be stored using lower-precision data types through a process known as quantization.

We distinguish two main families of weight quantization techniques in the literature:

    Post-Training Quantization (PTQ) is a straightforward technique where the weights of an already trained model are converted to lower precision without necessitating any retraining. Although easy to implement, PTQ is associated with potential performance degradation.
    Quantization-Aware Training (QAT) incorporates the weight conversion process during the pre-training or fine-tuning stage, resulting in enhanced model performance. However, QAT is computationally expensive and demands representative training data.

In this article, we focus on PTQ to reduce the precision of our parameters. To get a good intuition, we will apply both naïve and more sophisticated techniques to a toy example using a GPT-2 model.


# Доклад:

## Название доклада:
Large Language Model Quantization: как уменьшить размеры моделей и сохранить их работоспособность

## Описание доклада:
Доклад посвящен техникам квантования больших языковых моделей (LLMs), с акцентом на уменьшении размера моделей за счет изменения точности их весов.
Доклад охватывает основы квантования, преимущества и недостатки моделей сниженной точности, поиск и использование уже квантованных моделей, а также различные техники квантования.

## Полезное для слушателей:
1. Основы квантования и его применение к большим языковым моделям.
2. Преимущества и недостатки квантования моделей.
3. Поиск и использование уже квантованных моделей.
4. Техники квантования.

## Источники информации для подготовки к докладу:
- https://towardsdatascience.com/introduction-to-weight-quantization-2494701b9c0c
- https://www.tensorops.ai/post/what-are-quantized-llms
- https://huggingface.co/docs/optimum/concept_guides/quantization
- https://arxiv.org/pdf/2210.17323.pdf
- https://arxiv.org/pdf/2305.14314.pdf
- https://arxiv.org/pdf/1712.05877.pdf
- https://medium.com/intel-analytics-software/effective-post-training-quantization-for-large-language-models-with-enhanced-smoothquant-approach-93e9d104fb98 \\removed from copy as it is too long
- https://iq.opengenus.org/basics-of-quantization-in-ml/

## Вопрос к экзамену:
Квантование в контексте машинного обучения - это процесс уменьшения точности вычислений, который позволяет уменьшить требования к ресурсам при выполнении моделей. PTQ и QAT - это два основных подхода к квантованию. Какие преимущества и недостатки методов квантования Post-Training Quantization (PTQ) и Quantization-Aware Training (QAT)?

# Copy ready text:
Large Language Model Quantization: как уменьшить размеры моделей и сохранить их работоспособность

Доклад посвящен техникам квантования больших языковых моделей (LLMs), с акцентом на уменьшении размера моделей за счет изменения точности их весов.
Доклад охватывает основы квантования, преимущества и недостатки моделей сниженной точности, поиск и использование уже квантованных моделей, а также различные техники квантования.

1. Основы квантования и его применение к большим языковым моделям.
2. Преимущества и недостатки квантования моделей.
3. Post-Training Quantization (PTQ)
4. Quantization-Aware Training (QAT)
5. Использование уже квантованных моделей.

Источники информации для подготовки к докладу:
- https://towardsdatascience.com/introduction-to-weight-quantization-2494701b9c0c
- https://www.tensorops.ai/post/what-are-quantized-llms
- https://huggingface.co/docs/optimum/concept_guides/quantization
- https://arxiv.org/pdf/2210.17323.pdf
- https://arxiv.org/pdf/2305.14314.pdf
- https://arxiv.org/pdf/1712.05877.pdf
- https://iq.opengenus.org/basics-of-quantization-in-ml/

Вопрос к экзамену:
Квантование в контексте машинного обучения - это процесс уменьшения точности вычислений, который позволяет уменьшить требования к ресурсам при выполнении моделей. PTQ и QAT - это два основных подхода к квантованию. Какие преимущества и недостатки методов квантования Post-Training Quantization (PTQ) и Quantization-Aware Training (QAT)?