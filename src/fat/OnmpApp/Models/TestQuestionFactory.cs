using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Models;

public static class TestQuestionsFactory
{
    public static List<Question> CreateFromAttributes<T>(T card) where T : new()
    {
        var testQuestions = new List<Question>();

        var properties = typeof(T).GetProperties();

        foreach (var property in properties)
        {
            var radioButtonQuestionAttribute = property.GetCustomAttribute<RadioButtonQuestionAttribute>();
            var radioButtonWithTextQuestionAttribute = property.GetCustomAttribute<RadioButtonWithTextQuestionAttribute>();

            var checkBoxQuestionAttribute = property.GetCustomAttribute<CheckBoxQuestionAttribute>();
            var checkBoxWithTextQuestionAttribute = property.GetCustomAttribute<CheckBoxWithTextQuestionAttribute>();
            var textQuestionAttribute = property.GetCustomAttribute<TextQuestionAttribute>();

            bool assigned = false;

            if (radioButtonWithTextQuestionAttribute != null)
            {
                assigned = true;

                var radioButtonWithTextQuestion = new RadioButtonWithTextQuestion
                {
                    QuestionText = radioButtonWithTextQuestionAttribute.QuestionText,
                    Options = radioButtonWithTextQuestionAttribute.Options.ToList(),
                    AdditionalLabelText = radioButtonWithTextQuestionAttribute.AdditionalLabelText,
                    ResultType = radioButtonWithTextQuestionAttribute.ResultType
                };
                testQuestions.Add(radioButtonWithTextQuestion);
            }
            else if (radioButtonQuestionAttribute != null)
            {
                assigned = true;

                var radioButtonQuestion = new RadioButtonQuestion
                {
                    QuestionText = radioButtonQuestionAttribute.QuestionText,
                    Options = radioButtonQuestionAttribute.Options.ToList(),
                    AdditionalLabelText = radioButtonQuestionAttribute.AdditionalLabelText,

                };
                testQuestions.Add(radioButtonQuestion);
            }
            else if (checkBoxWithTextQuestionAttribute != null)
            {
                assigned = true;

                var checkBoxWithTextQuestion = new CheckBoxWithTextQuestion
                {
                    QuestionText = checkBoxWithTextQuestionAttribute.QuestionText,
                    Options = checkBoxWithTextQuestionAttribute.Options.ToList(),
                    SelectedOptions = new List<bool>(new bool[checkBoxWithTextQuestionAttribute.Options.Length]),
                    AdditionalLabelText = checkBoxWithTextQuestionAttribute.AdditionalLabelText,
                    ResultType = checkBoxWithTextQuestionAttribute.ResultType

                };

                testQuestions.Add(checkBoxWithTextQuestion);
            }
            else if (checkBoxQuestionAttribute != null)
            {
                assigned = true;

                var checkBoxQuestion = new CheckBoxQuestion
                {
                    QuestionText = checkBoxQuestionAttribute.QuestionText,
                    Options = checkBoxQuestionAttribute.Options.ToList(),
                    SelectedOptions = new List<bool>(new bool[checkBoxQuestionAttribute.Options.Length]),
                    AdditionalLabelText = checkBoxQuestionAttribute.AdditionalLabelText,
                };

                testQuestions.Add(checkBoxQuestion);
            }
            else if (textQuestionAttribute != null)
            {
                assigned = true;

                var textQuestion = new TextQuestion
                {
                    QuestionText = textQuestionAttribute.QuestionText,
                    ResultType = textQuestionAttribute.ResultType
                };

                testQuestions.Add(textQuestion);
            }

            if(assigned && card != null && property.GetValue(card) != null)
                testQuestions.Last().SetValue(property.GetValue(card).ToString());
        }

        return testQuestions;
    }
}
