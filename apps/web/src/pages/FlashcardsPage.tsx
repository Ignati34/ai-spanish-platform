import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';

export default function FlashcardsPage() {
  const { t } = useTranslation();
  const [text, setText] = useState('hola, gracias, por favor, buenos días, hasta luego');
  const [cards, setCards] = useState<any[]>([]);

  const generate = async () => {
    const r: any = await api.generateFlashcards(text);
    setCards(r.cards || r.deck?.cards || []);
  };

  return (
    <div>
      <PageHeader title={t('flashcards.title')} />
      <Card>
        <textarea className="h-24 w-full rounded-lg border border-slate-200 p-3 text-sm" value={text} onChange={(e) => setText(e.target.value)} />
        <Button className="mt-3" onClick={generate}>{t('flashcards.generate')}</Button>
      </Card>
      <div className="mt-5 grid gap-4 md:grid-cols-3">
        {cards.map((c, i) => (
          <Card key={i}><div className="text-lg font-medium">{c.front}</div><div className="mt-2 text-slate-500">{c.back}</div></Card>
        ))}
      </div>
    </div>
  );
}
