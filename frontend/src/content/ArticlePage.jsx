import ArticleLayout from "../layouts/articleLayout";

const ArticlePage = () => {
  return (
    <ArticleLayout
      kicker="Match Report"
      headline="Late strike sends Gira City through to the final"
      byline="By Amara Ngoy"
      publishedOn="August 23, 2026"
    >
      <p>
        A stoppage-time header settled a tense semi-final on Saturday, sending
        Gira City through to their first cup final in six years. The winner
        arrived in the fourth minute of added time, met on the volley from a
        deep corner after the visitors had spent much of the second half
        defending a narrow lead.
      </p>
      <p>
        It was a fitting end to a game that swung on fine margins throughout —
        a disallowed goal just after the break, two goal-line clearances, and
        a red card that left the visitors chasing the game with ten men for
        the final twenty minutes. The final is set for the first weekend of
        next month.
      </p>
    </ArticleLayout>
  );
};

export default ArticlePage;
