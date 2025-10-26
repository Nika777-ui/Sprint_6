import pytest
import allure

@allure.feature('FAQ раздел')
class TestFAQ:
    @allure.title('Проверка выпадающих списков FAQ')
    @pytest.mark.parametrize('question_number', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_faq_question(self, main_page, question_number):
        """Проверяем что при клике на вопрос появляется ответ"""
        with allure.step('Прокручиваем страницу к FAQ'):
            main_page.scroll_to_faq_section()
        
        with allure.step(f'Кликаем на вопрос {question_number}'):
            main_page.click_faq_question(question_number)
        
        with allure.step(f'Проверяем что ответ {question_number} отображается'):
            answer_text = main_page.get_faq_answer_text(question_number)
            assert answer_text != "", f"Ответ на вопрос {question_number} пустой"
            print(f"Вопрос {question_number}: {answer_text[:50]}...")