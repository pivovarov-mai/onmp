using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Models;

public abstract class TestQuestionAttribute : Attribute
{
    public string QuestionText { get; set; }
    public string[] Options { get; set; }
    public string AdditionalLabelText { get; set; }
    public Type ResultType { get; set; }

}

public interface ITextField
{
    public Type ResultType { get; set; }
}

public class RadioButtonQuestionAttribute : TestQuestionAttribute
{
    public RadioButtonQuestionAttribute(string questionText, string[] options, string additional = "")
    {
        QuestionText = questionText;
        Options = options;
        AdditionalLabelText = additional;
    }
}

public class RadioButtonWithTextQuestionAttribute : RadioButtonQuestionAttribute, ITextField
{

    public RadioButtonWithTextQuestionAttribute(string questionText, string[] options, string additional = "", Type resultType = null)
        : base(questionText, options, additional)
    {
        ResultType = resultType ?? typeof(string);
    }
}

public class CheckBoxQuestionAttribute : TestQuestionAttribute
{
    public CheckBoxQuestionAttribute(string questionText, string[] options, string additional = "")
    {
        QuestionText = questionText;
        Options = options;
        AdditionalLabelText = additional;
    }
}

public class CheckBoxWithTextQuestionAttribute : CheckBoxQuestionAttribute, ITextField
{

    public CheckBoxWithTextQuestionAttribute(string questionText, string[] options, string additional = "", Type resultType = null)
        : base(questionText, options, additional)
    {
        ResultType = resultType ?? typeof(string);
    }
}

public class TextQuestionAttribute : TestQuestionAttribute, ITextField
{

    public TextQuestionAttribute(string questionText, Type resultType = null)
    {
        QuestionText = questionText;
        ResultType = resultType ?? typeof(string);
    }
}