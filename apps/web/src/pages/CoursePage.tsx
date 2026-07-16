import { useTranslation } from 'react-i18next';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
export default function CoursePage() {
  const { t } = useTranslation();
  return (
    <div>
      <PageHeader title={t('nav.course')} />
      <div className="grid gap-4 md:grid-cols-3">
        {LEVELS.map((l) => (
          <Card key={l}><div className="flex items-center justify-between"><span className="text-xl font-semibold">{l}</span><Badge tone={l === 'A1' ? 'green' : 'slate'}>{l === 'A1' ? 'open' : 'locked'}</Badge></div></Card>
        ))}
      </div>
    </div>
  );
}
