import { ReactNode } from 'react';

/** A 3D flip card. Click (or the parent) toggles `flipped`; front/back are provided as nodes. */
export function FlipCard({ front, back, flipped, onClick, minHeight = 200 }: {
  front: ReactNode; back: ReactNode; flipped: boolean; onClick?: () => void; minHeight?: number;
}) {
  const face: React.CSSProperties = {
    position: 'absolute', inset: 0, backfaceVisibility: 'hidden', WebkitBackfaceVisibility: 'hidden',
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
    borderRadius: '1rem', border: '1px solid #e2e8f0', background: '#fff', padding: '1.5rem', textAlign: 'center',
  };
  return (
    <div onClick={onClick} style={{ perspective: 1200, cursor: onClick ? 'pointer' : 'default' }}>
      <div style={{ position: 'relative', minHeight, transformStyle: 'preserve-3d',
        transition: 'transform .5s', transform: flipped ? 'rotateY(180deg)' : 'none' }}>
        <div style={face}>{front}</div>
        <div style={{ ...face, transform: 'rotateY(180deg)' }}>{back}</div>
      </div>
    </div>
  );
}
