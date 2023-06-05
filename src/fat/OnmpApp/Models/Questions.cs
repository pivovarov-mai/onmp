using System.Text;
using CommunityToolkit.Mvvm.ComponentModel;
using OnmpApp.Properties;

namespace OnmpApp.Models;

public abstract class Question : ObservableObject
{
    public string QuestionText { get; set; }
    public List<string> Options { get; set; }
    public string AdditionalLabelText { get; set; } = "";
    public Type ResultType { get; set; } = typeof(string);


    public abstract string GetValue();
    public abstract void SetValue(string val);
    public abstract void CopyValue(Question question);

}

public partial class RadioButtonQuestion : Question
{
    [ObservableProperty]
    int selectedOptionIndex = -1;

    public override string GetValue()
    {
        return SelectedOptionIndex == -1 ? null : Options[SelectedOptionIndex];
    }

    public override void SetValue(string val)
    {
        SelectedOptionIndex = Options.IndexOf(val);
    }

    public override void CopyValue(Question question)
    {
        SelectedOptionIndex = ((RadioButtonQuestion)question).SelectedOptionIndex;
    }
}

public partial class RadioButtonWithTextQuestion : RadioButtonQuestion
{
    [ObservableProperty]
    string additionalText;

    public override string GetValue()
    {
        StringBuilder str = new();
        if (!string.IsNullOrEmpty(AdditionalLabelText))
        {
            if (SelectedOptionIndex >= 0)
                str.Append(Options[SelectedOptionIndex]);

            str.Append(Settings.FieldDelimeter + AdditionalLabelText + Settings.FieldDelimeter);

            AdditionalText = AdditionalText?.Trim();
            if (!string.IsNullOrEmpty(AdditionalText))
                str.Append(AdditionalText);

            if (str.ToString() == Settings.FieldDelimeter + AdditionalLabelText + Settings.FieldDelimeter)
                return null;
        }
        else
        {
            if (SelectedOptionIndex >= 0)
                str.Append(Options[SelectedOptionIndex]);
            else
                str.Append(AdditionalText);

            if (str.ToString().Trim() == "")
                return null;
        }

        return str.ToString();
    }

    public override void SetValue(string val)
    {
        if (!string.IsNullOrEmpty(AdditionalLabelText))
        {
            var splitStrings = val.Split(new[] { Settings.FieldDelimeter }, StringSplitOptions.None);
            SelectedOptionIndex = Options.IndexOf(splitStrings[0]);
            AdditionalLabelText = splitStrings[2];
        }
        else
        {
            SelectedOptionIndex = Options.IndexOf(val);
            if (SelectedOptionIndex == -1)
                AdditionalText = val;
        }
    }

    public override void CopyValue(Question question)
    {
        SelectedOptionIndex = ((RadioButtonWithTextQuestion)question).SelectedOptionIndex;
        AdditionalText = ((RadioButtonWithTextQuestion)question).AdditionalText;
    }
}

public partial class CheckBoxQuestion : Question
{
    [ObservableProperty]
    List<bool> selectedOptions;

    public override string GetValue()
    {
        StringBuilder str = new();
        for (var i = 0; i < Options.Count; i++)
            if (SelectedOptions[i])
            {
                str.Append(Options[i]);
                str.Append(Settings.PropertyDelimeter);
            }

        if (str.Length > 0)
            str.Length -= 1;

        return str.ToString();
    }

    public override void SetValue(string val)
    {
        var splitStrings = val.Split(new[] { Settings.PropertyDelimeter }, StringSplitOptions.None);

        for (var i = 0; i < splitStrings.Length; i++)
        {
            var ind = Options.IndexOf(splitStrings[i]);
            if (ind != -1)
                SelectedOptions[ind] = true;
        }
    }

    public override void CopyValue(Question question)
    {
        SelectedOptions = ((CheckBoxQuestion)question).SelectedOptions;
    }
}

public partial class CheckBoxWithTextQuestion : CheckBoxQuestion
{
    [ObservableProperty]
    string additionalText;

    public override string GetValue()
    {
        StringBuilder str = new();
        if (!string.IsNullOrEmpty(AdditionalLabelText))
        {
            for (var i = 0; i < SelectedOptions.Count; i++)
                if (SelectedOptions[i])
                    str.Append(Options[i] + Settings.PropertyDelimeter);
            if (str.Length > 0)
                str.Length -= 1;

            str.Append(Settings.FieldDelimeter + AdditionalLabelText + Settings.FieldDelimeter);

            AdditionalText = AdditionalText?.Trim();
            if (!string.IsNullOrEmpty(AdditionalText))
                str.Append(AdditionalText);

            if (str.ToString() == Settings.FieldDelimeter + AdditionalLabelText + Settings.FieldDelimeter)
                return null;
        }
        else
        {
            AdditionalText = AdditionalText?.Trim();
            if (!string.IsNullOrEmpty(AdditionalText))
                str.Append(AdditionalText);
            else
                for (var i = 0; i < SelectedOptions.Count; i++)
                    if (SelectedOptions[i])
                        str.Append(Options[i] + Settings.PropertyDelimeter);

            if (str.ToString().Trim() == "")
                return null;
        }

        return str.ToString();
    }

    public override void SetValue(string val)
    {
        if (!string.IsNullOrEmpty(AdditionalLabelText))
        {
            var splitStrings = val.Split(new[] { Settings.FieldDelimeter }, StringSplitOptions.None);

            var splitCheckBoxes = splitStrings[0].Split(new[] { Settings.PropertyDelimeter }, StringSplitOptions.None);
            for (var i = 0; i < splitCheckBoxes.Length; i++)
            {
                var id = Options.IndexOf(splitCheckBoxes[i]);
                if (id != -1)
                    SelectedOptions[id] = true;
            }

            if (splitStrings.Length > 1)
                AdditionalText = splitStrings[2];
        }
        else
        {
            if (val.Contains(Settings.PropertyDelimeter))
            {
                var splitCheckBoxes = val.Split(new[] { Settings.PropertyDelimeter }, StringSplitOptions.None);
                for (var i = 0; i < splitCheckBoxes.Length; i++)
                {
                    var id = Options.IndexOf(splitCheckBoxes[i]);
                    if (id != -1)
                        SelectedOptions[id] = true;
                }
            }
            else
            {
                AdditionalText = val;
            }
        }
    }

    public override void CopyValue(Question question)
    {
        SelectedOptions = ((CheckBoxWithTextQuestion)question).SelectedOptions;
        AdditionalText = ((CheckBoxWithTextQuestion)question).AdditionalText;
    }
}

public partial class TextQuestion : Question
{
    [ObservableProperty]
    string answerText;

    public override string GetValue()
    {
        AnswerText = AnswerText?.Trim();
        if (string.IsNullOrEmpty(AnswerText))
            return null;
        return AnswerText;
    }

    public override void SetValue(string val)
    {
        AnswerText = val;
    }

    public override void CopyValue(Question question)
    {
        AnswerText = ((TextQuestion)question).AnswerText;
    }
}

public class TestQuestionTemplateSelector : DataTemplateSelector
{
    public DataTemplate RadioButtonQuestionTemplate { get; set; }
    public DataTemplate RadioButtonWithTextQuestionTemplate { get; set; }
    public DataTemplate CheckBoxQuestionTemplate { get; set; }
    public DataTemplate CheckBoxWithTextQuestionTemplate { get; set; }
    public DataTemplate TextQuestionTemplate { get; set; }

    protected override DataTemplate OnSelectTemplate(object item, BindableObject container)
    {
        return item switch
        {
            RadioButtonWithTextQuestion => RadioButtonWithTextQuestionTemplate,
            RadioButtonQuestion => RadioButtonQuestionTemplate,
            CheckBoxWithTextQuestion => CheckBoxWithTextQuestionTemplate,
            CheckBoxQuestion => CheckBoxQuestionTemplate,
            TextQuestion => TextQuestionTemplate,
            _ => throw new NotSupportedException("Unknown question type")
        };
    }
}