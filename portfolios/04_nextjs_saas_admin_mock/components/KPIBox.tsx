type Props = { title: string; value: string };

export function KPIBox({ title, value }: Props) {
  return (
    <section>
      <strong>{title}</strong>
      <div>{value}</div>
    </section>
  );
}
